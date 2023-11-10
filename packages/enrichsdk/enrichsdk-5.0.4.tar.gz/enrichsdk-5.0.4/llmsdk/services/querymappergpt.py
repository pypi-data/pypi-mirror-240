from uuid import uuid4

import uvicorn
from fastapi.concurrency import run_in_threadpool
from .lib import *
from ..agents import LLMQueryMapper

logging.config.dictConfig(log_config)
logger = get_logger()

app = FastAPI()
app.agent = None

##############################################
# Common
##############################################
add_show_cache(app)
add_show_health(app)


@app.get("/up")
def up():
    return "Service is working!"


async def get_querymapper_agent():
    agentname = "querymappergpt"
    platform = "openai"
    querymapper_agent = LLMQueryMapper(name=agentname, platform=platform)

    logger.debug(f"Built agent for {agentname} and platform {platform}")

    return {
        "agent": querymapper_agent
    }


async def qna_run(request_id):
    cache = get_cache()

    if request_id not in cache:
        logger.error(f"Failure",
                     extra={
                         'request_id': "invalid",
                         "source": "service",
                     })
        cache[request_id] = {
            'status': "failure",
            "message": f"Invalid request id"
        }
        return

    # First get the params
    value = cache[request_id]

    try:

        params = value['params']
        user = params['user']
        dataset = params['dataset']
        query = params['query']

        stats['query_count'] += 1

        label = f"{user}_{dataset}"

        # First get the agent...
        logger.debug(f"Getting agent",
                     extra={
                         "source": "service",
                         "user": user,
                         "dataset": dataset,
                         "request_id": request_id,
                         'data': json.dumps(value, indent=4, cls=SafeEncoder)
                     })

        stats['datasets'][label] = {
            'loaded': datetime.now().replace(microsecond=0).isoformat(),
            'username': user,
            'agent_created': True,
            'agent_status': "Created",
            "query_count": 0,
            "query_success": 0,
            "query_failure": 0,
        }

        spec = get_profile_spec()

        # Now run the query
        result = await run_in_threadpool(lambda: app.agent.query(query, spec))

        if result.get("success"):
            key = result.get("key")
            logger.debug(f"Query: {query}\nKEY: {key}\n")
            json_result = json.loads(json.dumps(result, indent=4, cls=SafeEncoder))

            stats['query_success'] += 1
            stats['datasets'][label]['query_count'] += 1
            stats['datasets'][label]['query_success'] += 1
            query_update_result(request_id, {
                "status": "success",
                "result": json_result,
            })
        else:
            suggestions = result.get("suggestions")
            logger.debug(f"Query: {query}\nSuggestions: {suggestions}\n")
            json_result = json.loads(json.dumps(result, indent=4, cls=SafeEncoder))
            stats['datasets'][label]['query_count'] += 1
            stats['datasets'][label]['query_failure'] += 1
            query_update_result(request_id, {
                "status": "success",
                "result": json_result,
            })

    except Exception as e:
        stats['query_failure'] += 1
        stats['datasets'][label]['query_count'] += 1
        stats['datasets'][label]['query_failure'] += 1
        logger.exception(f"Failed to run query",
                         extra={
                             "source": "service",
                             'request_id': request_id,
                             "user": params.get('user', "unknown"),
                             "dataset": params.get('dataset', "unknown"),
                         })
        query_update_result(request_id, {
            "status": "failure",
            "answer": f"Unable to construct the answer. Could be an internal agent error. See the agent log",
            "result": {
                "text": str(e)
            }
        })


@app.get("/qna/status")
async def qna_status(request_id: str):
    """
    Get the status of the query request

    Parameters
    ----------
    request_id: str
                UUID generated for the request

    Returns
    -------
    status: dict
         Dictionary with request id, query, status, message and data
    """

    # First get the params
    try:

        cache = get_cache()

        if request_id not in cache:
            logger.error(f"Query Status: Invalid Request ID",
                         extra={
                             'request_id': request_id,
                             "source": "service",
                         })
            return {
                "request_id": request_id,
                "status": "failure",
                'answer': "Data not available. Either the request is invalid or the memory with that request has been cleared on restart"
            }

        value: dict = cache[request_id]
        status = value['status']
        logger.debug(f"Query Status: {status}",
                     extra={
                         "source": "service",
                         'request_id': request_id,
                         "dataset": value.get('dataset', 'unknown'),
                         "user": value.get('user', 'unknown'),
                         'data': json.dumps(value, indent=4, cls=SafeEncoder)
                     })

        return {
            "request_id": request_id,
            "query": value['query'],
            "status": value['status'],
            'message': value.get('message', ""),
            'data': value.get('result', {})
        }
    except Exception as e:
        return {
            "request_id": request_id,
            "query": value['query'],
            "status": "failure",
            "message": str(e),
            "data": {}
        }


@app.post("/qna")
async def classifier_qna(user: str,
                         query: str,
                         dataset: str,
                         background_tasks: BackgroundTasks,
                         mode: str = 'economy',
                         context: str = "",
                         namespace="querymappergpt",
                         policy: dict = {},
                         extra: dict = {}
                         ):
    cache = get_cache()
    request_id = str(uuid4())

    params = {
        "user": user,
        "dataset": dataset,
        "context": context,
        "namespace": namespace,
        "query": query,
        "policy": policy,
        "mode": mode
    }

    cache[request_id] = {
        'query': query,
        "status": "pending",
        "user": user,
        "dataset": dataset,
        "params": params
    }

    # Run the background task...
    background_tasks.add_task(qna_run, request_id)

    return {
        "request_id": request_id,
        "status": "pending",
        "query": query,
        "data": {}
    }


@app.on_event("startup")
async def app_startup():
    initialize_stats()

    if app.agent is None:
        details = await get_querymapper_agent()
        if details is None:
            query_update_result("request_id", {
                'status': "failure",
                "message": f"LLM QueryMapper Agent could not be found/built",
                "result": {}
            })
            return

        app.agent = details['agent']
        run_dir = stats.get('run_dir')
        index_name = "acme_gpt_index"
        persist_directory = os.path.join(run_dir, "index")
        spec = get_profile_spec()

        app.agent.load_spec(spec=spec,
                            persist_directory=persist_directory,
                            index_name=index_name)


def get_profile_spec():
    # ruleset
    RULE__TIME_PERIOD = "TIME_PERIOD must be one of 'day', 'week', 'month', 'quarter', or 'year'. Previous three months should be interpreted as a quarter."
    RULE__COUNTRY = "All COUNTRY names must be converted to 2 character ISO country codes"
    RULE__METRIC = "METRIC must be one of 'NSV' or 'NR'"

    # setup the template spec
    default = {
        "name": "acme_gpt",
        "topk": 5,
        "context": [
            "these queries are about cross-border financial transactions (traffic) at a fintech company",
            "GSV is a metric measuring sales volume",
            "NSV is a metric measuring sales volume",
            "NR is a metric measuring revenue"
        ],
        "templates": [
            {
                "template": "how many partners went live over the past TIME_PERIOD",
                "metadata": {
                    "key": "new_partners|TIME_PERIOD",
                    "rules": [
                        RULE__TIME_PERIOD
                    ],
                }
            },
            {
                "template": "what new B2B partners went live over the past TIME_PERIOD",
                "metadata": {
                    "key": "new_b2b_partners|TIME_PERIOD",
                    "rules": [
                        RULE__TIME_PERIOD
                    ],
                }
            },
            {
                "template": "which new source and/or destination countries have been launched this TIME_PERIOD",
                "metadata": {
                    "key": "new_countries|TIME_PERIOD",
                    "rules": [
                        RULE__TIME_PERIOD
                    ],
                }
            },
            {
                "template": "what is the trend of SOURCE_COUNTRY to DESTINATION_COUNTRY traffic over the last TIME_PERIOD",
                "metadata": {
                    "key": "traffic_trend|SOURCE_COUNTRY|DESTINATION_COUNTRY|TIME_PERIOD",
                    "rules": [
                        RULE__TIME_PERIOD,
                        RULE__COUNTRY
                    ],
                }
            },
            {
                "template": "what is the list of all partners in COUNTRY",
                "metadata": {
                    "key": "partners|COUNTRY",
                    "rules": [
                        RULE__COUNTRY
                    ],
                }
            },
            {
                "template": "what is the list of all source partners in COUNTRY",
                "metadata": {
                    "key": "source_partners|COUNTRY",
                    "rules": [
                        RULE__COUNTRY
                    ],
                }
            },
            {
                "template": "what is the list of all destination partners in COUNTRY",
                "metadata": {
                    "key": "dest_partners|COUNTRY",
                    "rules": [
                        RULE__COUNTRY
                    ],
                }
            },
            {
                "template": "what is the the list of banks or financial institutions in COUNTRY",
                "metadata": {
                    "key": "banks|COUNTRY",
                    "rules": [
                        RULE__COUNTRY
                    ],
                }
            },
            {
                "template": "how many senders and/or receivers have been serviced this TIME_PERIOD",
                "metadata": {
                    "key": "active_sndrs_rcvrs|TIME_PERIOD",
                    "rules": [
                        RULE__TIME_PERIOD
                    ],
                }
            },
            {
                "template": "what is the expected/projected sales metrics for this TIME_PERIOD",
                "metadata": {
                    "key": "expected_sales|TIME_PERIOD",
                    "rules": [
                        RULE__TIME_PERIOD
                    ],
                }
            },
            {
                "template": "what are the total sales for this TIME_PERIOD",
                "metadata": {
                    "key": "current_sales|TIME_PERIOD",
                    "rules": [
                        RULE__TIME_PERIOD
                    ],
                }
            },
            {
                "template": "rank destination countries based on METRIC from SOURCE_COUNTRY",
                "metadata": {
                    "key": "rank_dest_countries_from_source_country|METRIC|SOURCE_COUNTRY",
                    "rules": [
                        RULE__METRIC,
                        RULE__COUNTRY
                    ],
                }
            },
            {
                "template": "what was the sales volumes generated from new partners this TIME_PERIOD",
                "metadata": {
                    "key": "sales_new_partners|TIME_PERIOD",
                    "rules": [
                        RULE__TIME_PERIOD
                    ],
                }
            },
            {
                "template": "from how many countries were transactions received this TIME_PERIOD",
                "metadata": {
                    "key": "source_countries|TIME_PERIOD",
                    "rules": [
                        RULE__TIME_PERIOD
                    ],
                }
            },
            {
                "template": "to how many countries were transactions sent this TIME_PERIOD",
                "metadata": {
                    "key": "dest_countries|TIME_PERIOD",
                    "rules": [
                        RULE__TIME_PERIOD
                    ],
                }
            },
            {
                "template": "what are the highlights of business performance this TIME_PERIOD vs. last TIME_PERIOD",
                "metadata": {
                    "key": "highlights|TIME_PERIOD",
                    "rules": [
                        RULE__TIME_PERIOD
                    ],
                }
            },
            {
                "template": "what are the destination countries which were inactive over the last TIME_PERIOD",
                "metadata": {
                    "key": "inactive_destination_countries|TIME_PERIOD",
                    "rules": [
                        RULE__TIME_PERIOD
                    ],
                }
            },
            {
                "template": "what are the destination partners which were inactive over the last TIME_PERIOD",
                "metadata": {
                    "key": "inactive_destination_partners|TIME_PERIOD",
                    "rules": [
                        RULE__TIME_PERIOD
                    ],
                }
            },
            {
                "template": "what are the source countries that were inactive over the last TIME_PERIOD",
                "metadata": {
                    "key": "inactive_source_countries|TIME_PERIOD",
                    "rules": [
                        RULE__TIME_PERIOD
                    ],
                }
            },
            {
                "template": "what are the source partners who were inactive over the last TIME_PERIOD",
                "metadata": {
                    "key": "inactive_source_partners|TIME_PERIOD",
                    "rules": [
                        RULE__TIME_PERIOD
                    ],
                }
            },
        ]
    }

    return default


# For IDE Debugging
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10892)
