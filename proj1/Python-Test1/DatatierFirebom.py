import json
import argparse

parser = argparse.ArgumentParser(description='ArgumentParser for firebom generation tool')
parser.add_argument("--EnvironmentName", required=True, help="This is the EnvironmentName [Dev1,Dev2,QA1]")
parser.add_argument("--StackID", required=True, help="This is the StackID [101,102,201]")
parser.add_argument("--FalconInstance", required=True, help="This is the FalconInstance Name [azr-qa1-westus2]")
parser.add_argument("--EnvironmentID", required=True, help="This is the EnvironmentID [10]")
parser.add_argument("--FalconDomain", required=True, help="This is the FalconDomain Name [sfmc1]")
parser.add_argument("--ConfigFile", required=True, help="This is the path to the ConfigFile")
parser.add_argument("--outfile", required=True,  help="This is the path to the outputfile")

args = parser.parse_args()
print(args)
def BuildFireBom2(EnvironmentName:str, StackID: str, FalconInstance:str, EnvironmentID:str, FalconDomain:str,
                  ConfigFile:str, outfile: str):

    # Empty slate
    json_data = '''
    {
        "falcon_instance":{
           
        }
    }
    '''
    firebom_json = json.loads(json_data)

    # Read config file
    with open(ConfigFile, "r") as InstanceMapping:
        data = json.loads(InstanceMapping.read())

    # MI & DBFoundation resource Group
    firebom_json["falcon_instance"]["resource_group_name"] = f"{FalconInstance}-{data['resource_group_name']}"
    firebom_json["falcon_instance"]["dbfoundation_resource_group_name"] = f"{FalconInstance}-" \
                                                                          f"{data['dbfoundation_resource_group_name']}"

    # Turbo Related
    firebom_json["falcon_instance"]["turbo_image_name"] = f"{data['turbo_image_name']}"
    firebom_json["falcon_instance"]["turbo_identity"] = f"{FalconInstance}-{data['turbo_identity']}"
    firebom_json["falcon_instance"]["turbo_vm_name"] = f"azr-{EnvironmentName}-{data['turbo_vm_name']}"
    firebom_json["falcon_instance"]["turbo_vm_size"] = f"{data['turbo_vm_size']}"
    firebom_json["falcon_instance"]["turbo_app_name"] = f"{FalconInstance}-{data['turbo_app_name']}"
    firebom_json["falcon_instance"]["turbo_publish_folder_path"] = f"{data['turbo_publish_folder_path']}"

    #Default Tags
    firebom_json["falcon_instance"]["defaulttags"] = {}
    firebom_json["falcon_instance"]["defaulttags"]["stackid"]= StackID
    firebom_json["falcon_instance"]["defaulttags"]["env"] = EnvironmentName
    firebom_json["falcon_instance"]["defaulttags"]["envid"] = EnvironmentID


    # Function App
    for key in data['base_stack'].keys():
        if "dba" in key:
            funcapp_mi_name:str = key
            break
    for val in data['storage_container_names']:
        if "dbbackup" in val:
            funcapp_container_name = key
            break

    firebom_json["falcon_instance"]["functionapp"] = {}
    firebom_json["falcon_instance"]["functionapp"]["name"] = f"{FalconInstance}-{data['functionapp']['name']}"
    firebom_json["falcon_instance"]["functionapp"]["package_location"] = f"{data['functionapp']['package_location']}"
    firebom_json["falcon_instance"]["functionapp"]["package_name"] = f"{data['functionapp']['package_name']}"
    firebom_json["falcon_instance"]["functionapp"]["backup_container_name"] = funcapp_container_name
    firebom_json["falcon_instance"]["functionapp"]["mi_instance_name"] = f"{FalconInstance}-{FalconDomain}-smi-s{StackID}-" \
                                                                         f"{funcapp_mi_name}"

    # Storage
    firebom_json["falcon_instance"]["storage_ip_whitelist"] = data["storage_ip_whitelist"]
    firebom_json["falcon_instance"]["storage_sas_secret_name"] = data["storage_sas_secret_name"]
    firebom_json["falcon_instance"]["storage_container_names"] = {}
    for val in data['storage_container_names']:
        firebom_json["falcon_instance"]["storage_container_names"][val]={}
        firebom_json["falcon_instance"]["storage_container_names"][val]["container_name"]=val


    # AAD groups
    firebom_json["falcon_instance"]["datatier_database_aad_groups"] = {}
    firebom_json["falcon_instance"]["datatier_database_aad_groups"]["prefix"]=f"{FalconInstance}-{FalconDomain}"
    firebom_json["falcon_instance"]["datatier_database_aad_groups"]["suffix"]=\
        data["datatier_database_aad_groups"]["suffix"]
    firebom_json["falcon_instance"]["datatier_database_aad_groups"]["datatier_aad_group"] = \
        data["datatier_database_aad_groups"]["datatier_aad_group"]
    firebom_json["falcon_instance"]["datatier_database_aad_groups"]["datatier_reader_group"] = \
    data["datatier_database_aad_groups"]["datatier_reader_group"]
    firebom_json["falcon_instance"]["datatier_database_aad_groups"]["datatier_mi_aad_admin_group"] = \
    data["datatier_database_aad_groups"]["datatier_mi_aad_admin_group"]
    firebom_json["falcon_instance"]["datatier_database_aad_groups"]["groups"] = \
    data["datatier_database_aad_groups"]["groups"]

    # Adding managed Instance Base stack
    firebom_json["falcon_instance"]["base_stack"]={}
    for i,x in enumerate(data['base_stack']):
        newdata=data["base_stack"][f"{x}"]
        InstanceFqdn = f"{FalconInstance}-{FalconDomain}-smi-s{StackID}-{x}"
        newdata["instance_name"]=InstanceFqdn
        firebom_json["falcon_instance"]["base_stack"][f"{InstanceFqdn}"]= newdata

    # Adding managed Instance Cap Add
    firebom_json["falcon_instance"]["cap_add"] = {}
    for i, x in enumerate(data['cap_add']):
        newdata = data["cap_add"][f"{x}"]
        InstanceFqdn = f"{FalconInstance}-{FalconDomain}-smi-s{StackID}-{x}"
        newdata["instance_name"] = InstanceFqdn
        firebom_json["falcon_instance"]["cap_add"][f"{InstanceFqdn}"] = newdata

    # Adding dbbuild_pipeline
    firebom_json["falcon_instance"]["dbbuild_pipeline"]=data["dbbuild_pipeline"]

    # Write to file
    with open (outfile,"w+") as firebom:
        firebom.write(json.dumps(firebom_json, indent=2))

BuildFireBom2 (args.EnvironmentName, args.StackID, args.FalconInstance, args.EnvironmentID, args.FalconDomain,
               args.ConfigFile, args.outfile)
