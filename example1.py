import prefect
from prefect import task, Flow
from prefect.storage import GitHub
@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Hello, Cloud!")

with Flow("hello-flow") as flow:
    say_hello()

flow.storage = GitHub(
    repo="eugenberend/dag-tests",                           # name of repo
    path="example1.py"                   # location of flow file in repo
    #access_token_secret="GITHUB_ACCESS_TOKEN"  # name of personal access token secret
)

flow.register(project_name="Tutorial",labels=["common-k8s"])
