import argparse
import ast
import login
import projects
import versioned_items
import labels
import label_versions
import requests
import constants
import instances
import loginInput
from requests import Session
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
session = Session()
session.verify = False
#transport = Transport(session=session, timeout=10, operation_timeout=10)


# Method for parsing command line parameters
def parse_args():
    # Format for command line: subject verb flags
    # Options for first positional argument: login, label, labelVersion, project, versionedItems, instance, logout
    # Options for second positional argument: based on subject. Ex. label allows ls or create. instance allows only ls.
    parent_parser = argparse.ArgumentParser(
        description="description: sample Python CLI to perform queries using the GraphiQL API.")
    parent_parser.add_argument('--server', type=str, required=True,
                               help="provide link to GraphiQL API for the commands to run")
    subject_parser = parent_parser.add_subparsers(dest="subject",
                                                  description='''subjects description: The available subjects are stated below. To find out what actions can be performed on a subject, run python ci-cli.py [subject] -h. To run commands, the xauthtoken and server flags are required.''')

    # Subparser for login.
    login_parser = subject_parser.add_parser('login',
                                             description='''description: Login to MotioCI. There are two ways to run this command. 1. If no arguments are provided, the CLI will prompt the user to enter login information of instance name, namespace id, username and password. 2. The credentials flag and a properly formatted credentials string is provided. Examples of the login command using the credentials flag in either a windows/unix terminal are provided in the README.txt ''',
                                             help="login to MotioCI. Generates authtoken that will be used to run commands in the CLI.")
    login_parser.add_argument('--credentials', type=str,
                              help="alternate method of login. Allows user to login using a properly formatted credentials string.",
                              metavar='')

    # Subparser for instance subject. Commands available: ls
    instance_subparser = subject_parser.add_parser("instance", help="perform queries on instances.",
                                                   description="description: perform queries on instances.")
    instance_verb_subparser = instance_subparser.add_subparsers(dest="verb")
    instance_ls_parser = instance_verb_subparser.add_parser("ls",
                                                            help="list all instances that the user has access to.",
                                                            description='''description: List instances. There is only one way to run this command. 1. When no arguments are present, list all instances that the user has access to. ''')
    instance_ls_parser.add_argument('--xauthtoken', type=str, required=True,
                                    help="login token given after performing login command correctly.")

    # Subparser for project subject. Commands available: ls
    project_subparser = subject_parser.add_parser("project", help="perform queries on projects.",
                                                  description="description: perform queries on projects.")
    project_verb_subparser = project_subparser.add_subparsers(dest="verb")
    project_ls_parser = project_verb_subparser.add_parser("ls",
                                                          description='''description: List projects. There are two ways to run this command. 1. When no arguments are present, list all projects that the user has access to. 2. With argument instanceName present, list only projects that exist within the instance that matches the instanceName.''',
                                                          help="list all projects that the user has access to.")
    project_ls_parser.add_argument('--xauthtoken', type=str, required=True,
                                   help="login token given after performing login command correctly.")
    project_ls_parser.add_argument('--instanceName', type=str, help="query based on specific instance name.",
                                   metavar='')

    # Subparsers for label subject. Commands available: create and ls
    label_subparser = subject_parser.add_parser("label", help="perform queries/mutation on labels.",
                                                description="description: perform queries/mutation on labels.")
    label_verb_subparser = label_subparser.add_subparsers(dest="verb")
    label_create_parser = label_verb_subparser.add_parser("create", help="create a new label.",
                                                          description='''
                                                          description: Create a new label. There is only one way to run this command. 1. With arguments instanceName, projectName, name,
                                                          and versionedItemIds present, create a new label from the given arguments. ''')
    label_create_parser.add_argument('--xauthtoken', type=str, required=True,
                                     help="login token given after performing login command correctly.")
    label_create_parser.add_argument('--instanceName', type=str, metavar='', help="used to find instance id.")
    label_create_parser.add_argument('--projectName', type=str, metavar='', help="used to find project id.")
    label_create_parser.add_argument('--name', type=str, metavar='', help="creates a label with this name.")
    label_create_parser.add_argument('--versionedItemIds', type=str, metavar='',
                                     help="list of items to include under the new label.")
    label_ls_parser = label_verb_subparser.add_parser("ls", help="list all labels that the user has access to.",
                                                      description='''description: List labels. There are three ways to run this command. 1. When no arguments are present, list all labels that the user has access to. 2. With arguments instanceName and projectName present, list all labels within the given instance and project. 3. With argument labelName present, list the label with matching labelName.''')
    label_ls_parser.add_argument('--xauthtoken', type=str, required=True,
                                 help="login token given after performing login command correctly.")
    label_ls_parser.add_argument('--instanceName', type=str, help="query based on specific instance name.", metavar='')
    label_ls_parser.add_argument('--projectName', type=str, help="query based on specific project name.", metavar='')
    label_ls_parser.add_argument('--labelName', type=str, help="query based on specific label name.", metavar='')

    # Subparsers for label version subject. Commands available: promote and ls
    label_version_subparser = subject_parser.add_parser("labelVersion",
                                                        description="description: perform queries/mutation on label versions.",
                                                        help="perform queries/mutation on label versions.")
    label_version_verb_subparser = label_version_subparser.add_subparsers(dest="verb")
    label_version_promote_parser = label_version_verb_subparser.add_parser("promote", help="promote a label.",
                                                                           description=''' description: promote a label. There are two ways to run this command. 1.if no arguments are provided, the program will automatically prompt the user to input relevant information to perform the query. 2.With some or all arguments given, the CLI will prompt user to input critical information such as target instance id and label version id.''')

    label_version_promote_parser.add_argument('--xauthtoken', type=str, required=True,
                                              help="login token given after performing login command correctly.")
    label_version_promote_parser.add_argument('--sourceInstanceName', type=str, metavar='',
                                              help="used to find source instance id.")
    label_version_promote_parser.add_argument('--targetInstanceName', type=str, metavar='',
                                              help="used to find target instance id.")
    label_version_promote_parser.add_argument('--projectName', type=str, metavar='', help="used to find project id.")
    label_version_promote_parser.add_argument('--labelName', type=str, metavar='', help="used to find label id.")
    label_version_promote_parser.add_argument('--sourceInstanceId', type=int, metavar='',
                                              help="specify source instance.")
    label_version_promote_parser.add_argument('--targetInstanceId', type=int, metavar='',
                                              help="specify target instance.")
    label_version_promote_parser.add_argument('--projectId', type=int, metavar='', help="specify project.")
    label_version_promote_parser.add_argument('--labelId', type=int, metavar='', help="specify label.")
    label_version_promote_parser.add_argument('--labelVersionId', type=int, metavar='',
                                              help="used to find specific label version.")
    label_version_promote_parser.add_argument('--version', type=int, metavar='', help="used to find version of label.")
    label_version_promote_parser.add_argument('--versionedItemIds', type=str, metavar='',
                                              help="create a new label with these versioned items")
    label_version_promote_parser.add_argument('--searchPath', nargs='+', type=str, action='append', metavar='',
                                              help="used to find versioned items located by path")

    label_version_ls_parser = label_version_verb_subparser.add_parser("ls",
                                                                      help="list label versions that the user has access to.",
                                                                      description='''
                                                        description: List label versions.There are two ways to call this verb: 1.With no arguments present,
                                                        list all of the label versions that the user has access to.2.With arguments
                                                         instanceName, projectName, and labelName present, lists the label versions that fit the criteria within the instance, project, and label names.
                                                        ''')

    label_version_ls_parser.add_argument('--xauthtoken', type=str, required=True,
                                         help="login token given after performing login command correctly.")
    label_version_ls_parser.add_argument('--instanceName', type=str, help="query based on specific instance name.",
                                         metavar='')
    label_version_ls_parser.add_argument('--projectName', type=str, help="query based on specific project name.",
                                         metavar='')
    label_version_ls_parser.add_argument('--labelName', type=str, help="query based on specific label name.",
                                         metavar='')

    # Subparser for versioned item subject. Commands available: ls
    versioned_item_subparser = subject_parser.add_parser("versionedItems",
                                                         help="perform queries on versioned items.")
    versioned_item_verb_subparser = versioned_item_subparser.add_subparsers(dest="verb")
    versioned_item_ls_parser = versioned_item_verb_subparser.add_parser("ls", help='''
        list versioned items content.''',
                                                                        description=''' description: list versioned items. There are two ways to call this verb: 1.With no arguments present, list all of the label versions that the user has access to. 2.With arguments instanceName, projectName, searchPath, and currentOnly present, list the label versions with match the criteria. The search path has to be formatted in a special way: 'operator:path/to/the/file'. The operator can be starts, contains, equals, ends, between, and in.''')

    versioned_item_ls_parser.add_argument('--xauthtoken', type=str, required=True,
                                          help="login token given after performing login command correctly.")
    versioned_item_ls_parser.add_argument('--instanceName', type=str, help="query based on specific instance name.",
                                          metavar='')
    versioned_item_ls_parser.add_argument('--projectName', type=str, help="query based on specific project name.",
                                          metavar='')
    versioned_item_ls_parser.add_argument('--searchPath', type=str,
                                          help="query for versioned items based on their path in CI. Able to input many search paths with a space between them.",
                                          metavar='')
    versioned_item_ls_parser.add_argument('--currentOnly', type=bool,
                                          help="determines what types of versioned items are displayed. if true, display only non-deleted versioned items. if false, display all versioned items.",
                                          metavar='')

    # Subparser for logout subject.
    logout_subparser = subject_parser.add_parser("logout",
                                                 help="logout of MotioCI. The authtoken will be unusable afterwards.",
                                                 description='''logout of MotioCI. There is only one way to run this command. With no arguments, this will log you out of MotioCI and the authtoken will be unusable afterwards ''')
    logout_subparser.add_argument('--xauthtoken', type=str, required=True,
                                  help="login token given after performing login command correctly.")
    return parent_parser.parse_args()


def label_version_promotion(args):
    # Minimum required arguments for deploy label: target_instance_id and label_version_id.
    target_instance_id = args.targetInstanceId
    label_version_id = args.labelVersionId
    # Loop for id, name, or user input for target_instance, source_instance, and project.
    target_instance_name = args.targetInstanceName
    target_instance_id = find_instance_id(target_instance_id, target_instance_name, "Enter Target Instance Name/Id: ")
    # Check if labelVersionId is given. Skip to promoting label if given.
    if args.labelVersionId is None:
        label_id = args.labelId
        # Check if labelId is given. Skip to querying for latest version id if given. Else, find label id
        if args.labelId is None:
            source_instance_id = args.sourceInstanceId
            source_instance_name = args.sourceInstanceName
            project_id = args.projectId
            project_name = args.projectName
            label_name = args.labelName
            source_instance_id = find_instance_id(source_instance_id, source_instance_name,
                                                  "Enter Source Instance Name/Id: ")
            project_id = find_project_id(source_instance_id, project_id, project_name, "Enter Project Name/Id: ")
            # Find label id using project_id and labelName
            if label_name is None:
                label_name = input("Enter Label Name: ")
            label_id_list = labels.get_label_id(project_id, label_name)
            # Label id was not found. Check if versionedItemsId or searchPath were given to create new label.
            if label_id_list is None:
                versioned_item_ids = get_versioned_items(args, project_id)
                label_id = labels.create_label_if_not_exist(project_id, label_name, versioned_item_ids)
            else:
                label_id = label_id_list[0]["node"]["id"]
        # Get the latest label_version_id using label_id. Check if a specific version is given
        if args.version is None:
            label_version_id = label_versions.get_version_id_default(label_id)
        else:
            label_version_id = label_versions.get_version_id_specific(label_id, args.version)
    # call promote label
    label_versions.promote_label_version_call(target_instance_id, label_version_id)
    return


# Loop for instances' id, name, or valid user input. Validates user input on possible options in CI
def find_instance_id(instance_id, instance_name, input_string):
    outputOptionsAvailable = False
    instance_array = instances.get_instances_default()
    while True:
        if instance_id is None:
            if instance_name is None:
                if outputOptionsAvailable is True:
                    instance_array = instances.get_instances_default()
                    print("Error! Incorrect Input!")
                    print("Available entries: ", end="")
                    instances.print_instances(instance_array)
                    print("")
                user_input = input(input_string)
                outputOptionsAvailable = True
                instance_id, instance_name = assign_input(user_input)

        if instance_id is not None:
            if instances.check_if_valid_instance_id(instance_array, instance_id):
                break

        elif instance_name is not None:
            if instances.check_if_valid_instance_name(instance_array, instance_name):
                instance_id = instances.get_instance_id(instance_name)
                break

        instance_id = None
        instance_name = None
    return instance_id


# Loop for projects' id, name, or valid user input. Validates user input on possible options in CI
def find_project_id(source_instance_id, project_id, project_name, input_string):
    outputOptionsAvailable = False
    project_list = projects.get_valid_projects(source_instance_id)
    while True:
        if project_id is None:
            if project_name is None:
                if outputOptionsAvailable is True:
                    print("Error! Incorrect Input!")
                    print("Available entries: ", end="")
                    project_list = projects.get_valid_projects(source_instance_id)
                    projects.print_projects(project_list)
                    print("")
                user_input = input(input_string)
                outputOptionsAvailable = True
                project_id, project_name = assign_input(user_input)

        if project_id is not None:
            if projects.check_if_valid_project_id(project_list, project_id):
                break

        elif project_name is not None:
            if projects.check_if_valid_project_name(project_list, project_name):
                project_id = projects.get_project_id(source_instance_id, project_name)
                break

        project_id = None
        project_name = None
    return project_id


# Sets id if userinput is type int. Else sets name
def assign_input(user_input):
    try:
        int_input = int(user_input)
        return int_input, None
    except ValueError:
        return None, user_input


# Loop for user input of versioned_item_ids
def get_user_input_versioned_item_ids():
    versioned_item_ids = []
    print("Enter versionedItemIds. Press q to stop:")
    curId = ""
    while True:
        curId = input("Enter id:")
        if curId == "q":
            break
        response = versioned_items.get_versioned_item_by_id(int(curId))
        if response["data"]["versionedItem"] is None:
            print("Bad versionedItemId, enter another one")
            continue
        versioned_item_ids.append(int(curId))
    return versioned_item_ids


# Retrieve versioned item ids from search path inputted by user
def get_user_input_search_path(project_id):
    versioned_item_ids = []
    print("Enter search path. Press q to stop:")
    curPath = ""
    while True:
        curPath = input("Enter path:")
        if curPath == "q":
            break
        if curPath == "":
            continue
        response = ast.literal_eval(label_versions.get_version_ids(project_id, [[curPath]]))
        if len(response) == 0:
            print("Bad searchpath, enter another one")
            continue
        versioned_item_ids.extend(response)
    print("final versioned item list:", list(set(versioned_item_ids)))
    return list(set(versioned_item_ids))


# Retrieve versioned_items from either versionedItemIds, searchPath, or both. Ask for user input if both fields are None
def get_versioned_items(args, project_id):
    versioned_item_ids = []
    # If search path is given, find versioned_item_ids
    if args.searchPath is not None:
        versioned_item_ids.extend(ast.literal_eval(label_versions.get_version_ids(project_id, args.searchPath)))
    if args.versionedItemIds is not None:
        versioned_item_ids.extend(ast.literal_eval(args.versionedItemIds))
    if args.versionedItemIds is None and args.searchPath is None:
        versioned_item_ids = get_user_input_search_path(project_id)
    return versioned_item_ids


'''
List of if elif else statements for deciding which method to execute based on input.
args.subject options: login, instance, project, label, label version, versioned items, and logout
args.verb options: ls, create (label only), promote (label version only)
Each ls has a default option with no flags (except --authtoken) and a specific option with all flags needed to execute
Each create and promote label requires all flags.
'''

args = parse_args()
constants.CI_URL = args.server
constants.LOGIN_URL = constants.CI_URL + constants.LOGIN_URL
constants.LOGOUT_URL = constants.CI_URL + constants.LOGOUT_URL
constants.GRAPH_URL = constants.CI_URL + constants.GRAPH_URL

if args.subject == "login":
    if args.credentials is None:
        args.credentials = loginInput.get_login_from_user()
    auth_token = login.login_init(args.credentials)
    if auth_token is None:
        print("Invalid credentials. Login aborted!")
    else:
        print("Credentials: ", args.credentials)
        print("Login successful!")
        print("x-auth_token: ", auth_token)


else:
    constants.X_AUTH_TOKEN = args.xauthtoken
if args.subject == "instance":
    if args.verb == "ls":
        print(instances.get_instances_default())
elif args.subject == "project":
    if args.verb == "ls":
        if args.instanceName is not None:
            projects.get_projects_specific(args.instanceName)
        else:
            projects.get_projects_default()
elif args.subject == "label":
    if args.verb == "create":
        labels.create_label_init(args.instanceName, args.projectName, args.name, args.versionedItemIds)
        print("Label Created!")
    elif args.verb == "ls":
        if args.labelName is not None:
            labels.get_label_specific(args.instanceName, args.projectName, args.labelName)
        elif args.instanceName is not None and args.projectName is not None:
            labels.get_labels_specific(args.instanceName, args.projectName)
        else:
            labels.get_labels_default()
elif args.subject == "labelVersion":
    if args.verb == "promote":
        # no if else statements
        label_version_promotion(args)
        print("Promoted!")
    elif args.verb == "ls":
        if args.instanceName is not None and args.projectName is not None and args.labelName is not None:
            label_versions.get_label_version_specific(args.instanceName, args.projectName,
                                                      args.labelName)
        else:
            label_versions.get_label_version_default()

elif args.subject == "versionedItems":
    if args.verb == "ls":
        if args.instanceName is not None and args.projectName is not None and args.searchPath is not None and args.currentOnly is not None:
            versioned_items.get_versioned_items_specific(args.instanceName, args.projectName,
                                                         args.searchPath, args.currentOnly)
        else:
            versioned_items.get_versioned_items_default()
elif args.subject == "logout":
    response = requests.post(constants.LOGOUT_URL, headers={'x-auth-token': constants.X_AUTH_TOKEN}, verify=False)
    print("Logged out!")
