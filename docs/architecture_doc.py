from diagrams import Cluster, Diagram
from diagrams.programming.language import Python
from diagrams.aws.compute import EC2
from diagrams.custom import Custom

graph_attr = {
    "bgcolor": "transparent",
    "pad": "0.5"
}

with Diagram(name="", show=False, graph_attr=graph_attr, filename="./docs/architecture_image"):

    with Cluster("",graph_attr = {
    "bgcolor": "azure3"
}):

        (
            EC2("Your API") >> 
            Python("SCTS") >> 
            Custom("Correios", icon_path="./images/correios-logo.png") # << Python("SCTS")
        )