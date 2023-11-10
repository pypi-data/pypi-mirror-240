import argparse
from avala.client import APIClient
from avala.utils import ConfigValidator

def main():
    parser = argparse.ArgumentParser(description='Avala Client SDK.')

    subparsers = parser.add_subparsers(title="Operations", dest="operation")

    import_parser = subparsers.add_parser("dataset-import", help="Import a dataset")

    import_parser.add_argument("--name", required=True, help="Name of dataset")
    import_parser.add_argument('--visibility', default='public', help='Visibility of the dataset')
    import_parser.add_argument('--industry', required=True, type=str, help='Industry code')
    import_parser.add_argument('--license', required=True, type=str, help='License code')
    import_parser.add_argument('--citation', required=False, type=str, help='Citation for the dataset')
    import_parser.add_argument('--creator', required=True, type=str, help='Creator of the dataset')
    import_parser.add_argument('--description', required=True, type=str, help='Description of the dataset')

    license_parser = subparsers.add_parser("get-licenses", help="List available licenses")
    industry_parser = subparsers.add_parser("get-industries", help="List available industries")

    list_datasets_parser = subparsers.add_parser("get-datasets", help="List my datasets")
    list_projects_parser = subparsers.add_parser("get-projects", help="List my projects")

    annotations_parser = subparsers.add_parser("annotation-import", help="Import annotations of an existing dataset")
    annotations_parser.add_argument("--dataset-uid", required=True, help="Unique identifier for dataset")
    annotations_parser.add_argument("--annotations-file", required=True, help="The path to json file containing annotations in Coco format")
    annotations_parser.add_argument("--keep-annotations", required=False, default=False, help="Whether to keep any previous annotations for the project")
    annotations_parser.add_argument("--project-name", required=True, help="The Avala project to link these imported annotations to")

    list_exports_parser = subparsers.add_parser("get-annotation-exports", help="List my results")

    args = parser.parse_args()

    validator = ConfigValidator()
    if not validator.validate_config():
        print("Invalid config.json file. Please fix it")
        exit()
    elif validator.requires_importing_creds():
        if not validator.import_google_creds():
            print("Error importing google_auth_creds.json file")
            exit()

    client = APIClient(validator.get_config())

    if args.operation == "dataset-import":
        if not client.is_dataset_name_valid(args.name):
            print("Dataset name is invalid or already exists. Please try a different name")
        else:
            client.import_dataset(args)
    elif args.operation == "get-licenses":
        response = client.get_licenses()
        client.show(response)
    elif args.operation == "get-industries":
        response = client.get_industries()
        client.show(response)
    elif args.operation == "get-datasets":
        response = client.get_datasets()
        client.show(response)
    elif args.operation == "get-projects":
        response = client.get_projects()
        client.show(response)
    elif args.operation == "annotation-import":
        client.import_annotations(args)
    elif args.operation == "get-annotation-exports":
        response = client.get_exports()
        print(response)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

