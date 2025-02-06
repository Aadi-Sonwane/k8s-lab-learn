
import os

# Define the complete folder structure
folder_structure = {
    'docs': {
        'Introduction': {
            'Cluster_Components': {
                'examples': ['Cluster_Components.md', 'Cluster_Components.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Installation': {
                'examples': ['Installation.md', 'Installation.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Kubernetes_Architecture': {
                'examples': ['Kubernetes_Architecture.md', 'Kubernetes_Architecture.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Overview': {
                'examples': ['Overview.md', 'Overview.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            }
        },
        'Core_Concepts': {
            'ConfigMaps': {
                'examples': ['ConfigMaps.md', 'ConfigMaps.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Deployments': {
                'examples': ['Deployments.md', 'Deployments.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Endpoints': {
                'examples': ['Endpoints.md', 'Endpoints.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Namespaces': {
                'examples': ['Namespaces.md', 'Namespaces.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Persistent_Volumes': {
                'examples': ['Persistent_Volumes.md', 'Persistent_Volumes.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Persistent_Volume_Claims': {
                'examples': ['Persistent_Volume_Claims.md', 'Persistent_Volume_Claims.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Pods': {
                'examples': ['Pods.md', 'Pods.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'ReplicaSets': {
                'examples': ['ReplicaSets.md', 'ReplicaSets.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Secrets': {
                'examples': ['Secrets.md', 'Secrets.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Services': {
                'examples': ['Services.md', 'Services.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Volumes': {
                'examples': ['Volumes.md', 'Volumes.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            }
        },
        'Workloads': {
            'CronJobs': {
                'examples': ['CronJobs.md', 'CronJobs.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'DaemonSets': {
                'examples': ['DaemonSets.md', 'DaemonSets.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Deployments': {
                'examples': ['Deployments.md', 'Deployments.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Jobs': {
                'examples': ['Jobs.md', 'Jobs.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Pod_Disruption_Budgets': {
                'examples': ['Pod_Disruption_Budgets.md', 'Pod_Disruption_Budgets.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'ReplicaSet': {
                'examples': ['ReplicaSet.md', 'ReplicaSet.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'StatefulSets': {
                'examples': ['StatefulSets.md', 'StatefulSets.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
        },
        'Networking': {
            'CNI_Container_Network_Interface': {
                'examples': ['CNI_Container_Network_Interface.md', 'CNI_Container_Network_Interface.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'DNS': {
                'examples': ['DNS.md', 'DNS.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Ingress': {
                'examples': ['Ingress.md', 'Ingress.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'LoadBalancers': {
                'examples': ['LoadBalancers.md', 'LoadBalancers.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Networking_Concepts': {
                'examples': ['Networking_Concepts.md', 'Networking_Concepts.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Network_Policies': {
                'examples': ['Network_Policies.md', 'Network_Policies.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Services': {
                'examples': ['Services.md', 'Services.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Service_Mesh': {
                'examples': ['Service_Mesh.md', 'Service_Mesh.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
        },
        'Security': {
            'Network_Policies': {
                'examples': ['Network_Policies.md', 'Network_Policies.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Pod_Security_Policies': {
                'examples': ['Pod_Security_Policies.md', 'Pod_Security_Policies.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'RBAC_Role_Based_Access_Control': {
                'examples': ['RBAC_Role_Based_Access_Control.md', 'RBAC_Role_Based_Access_Control.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Secrets_Management': {
                'examples': ['Secrets_Management.md', 'Secrets_Management.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Security_Context': {
                'examples': ['Security_Context.md', 'Security_Context.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Service_Accounts': {
                'examples': ['Service_Accounts.md', 'Service_Accounts.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
        },
        'Storage': {
            'Dynamic_Provisioning': {
                'examples': ['Dynamic_Provisioning.md', 'Dynamic_Provisioning.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Persistent_Volumes': {
                'examples': ['Persistent_Volumes.md', 'Persistent_Volumes.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'StatefulSets': {
                'examples': ['StatefulSets.md', 'StatefulSets.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Storage_Classes': {
                'examples': ['Storage_Classes.md', 'Storage_Classes.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Volumes': {
                'examples': ['Volumes.md', 'Volumes.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
        },
         'Cluster_Management': {
            'Cluster_Autoscaler': {
                'examples': ['Cluster_Autoscaler.md', 'Cluster_Autoscaler.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Cluster_Setup': {
                'examples': ['Cluster_Setup.md', 'Cluster_Setup.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'High_Availability_Setup': {
                'examples': ['High_Availability_Setup.md', 'High_Availability_Setup.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Kubeadm': {
                'examples': ['Kubeadm.md', 'Kubeadm.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'kubectl_CLI': {
                'examples': ['kubectl_CLI.md', 'kubectl_CLI.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Managing_Nodes': {
                'examples': ['Managing_Nodes.md', 'Managing_Nodes.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Node_Pools': {
                'examples': ['Node_Pools.md', 'Node_Pools.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
        },
        'Advanced_Topics': {
            'API_Aggregation_Layer': {
                'examples': ['API_Aggregation_Layer.md', 'API_Aggregation_Layer.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Custom_Resources': {
                'examples': ['Custom_Resources.md', 'Custom_Resources.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Helm': {
                'examples': ['Helm.md', 'Helm.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Horizontal_Pod_Autoscaling': {
                'examples': ['Horizontal_Pod_Autoscaling.md', 'Horizontal_Pod_Autoscaling.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Kubernetes_Federation': {
                'examples': ['Kubernetes_Federation.md', 'Kubernetes_Federation.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Operators': {
                'examples': ['Operators.md', 'Operators.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Vertical_Pod_Autoscaling': {
                'examples': ['Vertical_Pod_Autoscaling.md', 'Vertical_Pod_Autoscaling.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
        },
        'Monitoring_and_Logging': {
            'ELK_Stack': {
                'examples': ['ELK_Stack.md', 'ELK_Stack.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Fluentd': {
                'examples': ['Fluentd.md', 'Fluentd.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Grafana': {
                'examples': ['Grafana.md', 'Grafana.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Monitoring_Tools': {
                'examples': ['Monitoring_Tools.md', 'Monitoring_Tools.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Prometheus': {
                'examples': ['Prometheus.md', 'Prometheus.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
        },
        'Troubleshooting': {
            'Common_Issues': {
                'examples': ['Common_Issues.md', 'Common_Issues.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Debugging_Pods': {
                'examples': ['Debugging_Pods.md', 'Debugging_Pods.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Logs_and_Events': {
                'examples': ['Logs_and_Events.md', 'Logs_and_Events.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
        },
        'CI_CD': {
            'GitLab_CI': {
                'examples': ['GitLab_CI.md', 'GitLab_CI.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Jenkins': {
                'examples': ['Jenkins.md', 'Jenkins.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
        },
        'Cloud_Integrations': {
            'AWS': {
                'examples': ['AWS.md', 'AWS.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Azure': {
                'examples': ['Azure.md', 'Azure.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Google_Cloud': {
                'examples': ['Google_Cloud.md', 'Google_Cloud.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
        },
        'Future_Trends_and_Community': {
            'Community_Resources': {
                'examples': ['Community_Resources.md', 'Community_Resources.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Contributors': {
                'examples': ['Contributors.md', 'Contributors.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Future_Trends': {
                'examples': ['Future_Trends.md', 'Future_Trends.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
        },
        'Resources': {
            'Books': {
                'examples': ['Books.md', 'Books.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Courses': {
                'examples': ['Courses.md', 'Courses.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
            'Websites': {
                'examples': ['Websites.md', 'Websites.yml'],
                'labs': ['labs.md', 'labs.yml'],
                'use_cases': ['use_cases.md', 'use_cases.yml']
            },
        },
    }
}

# Function to create folders and files
def create_folders_and_files(base_path, structure):
    for folder, substructure in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        if isinstance(substructure, dict):
            create_folders_and_files(folder_path, substructure)
        elif isinstance(substructure, list):
            for file_name in substructure:
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'w') as f:
                    f.write(f"### {file_name} - Placeholder Content")

# Function to create mkdocs.yml file
def create_mkdocs_yml(base_path):
    mkdocs_content = """site_name: Kubernetes Documentation
site_url: https://your-site-url.com
theme:
    name: 'material'
nav:
    - Home: index.md
"""
    # Generating navigation for each section
    for section, subfolder in folder_structure['docs'].items():
        mkdocs_content += f"    - {section}:\n"
        for subsection, subfolder in subfolder.items():
            mkdocs_content += f"        - {subsection}: {section}/{subsection}/examples/{subsection}.md\n"
    
    with open(os.path.join(base_path, 'mkdocs.yml'), 'w') as f:
        f.write(mkdocs_content)

# Define the base path for the project folder
base_path = '.'

# Create the folder structure and files
create_folders_and_files(base_path, folder_structure)

# Create the mkdocs.yml file
create_mkdocs_yml(base_path)

print(f"Folder structure and mkdocs.yml have been created successfully at {base_path}.")