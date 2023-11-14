import json
import sys
from rich.console import Console
from rich.table import Table
import os
from cement import Controller, ex

import perian
from perian.models.flavor_query import FlavorQuery
from perian.models.provider_name import ProviderName

def print_flavor_results(flavors, app, minimal_ui=False, green_energy=False):
    if len(flavors) > 0:
        table = Table()
        columns = []

        if minimal_ui and not green_energy:
            columns = ["Provider", "CPU Cores", "RAM", "GPU", "Location", "Price (€/h)"]
        elif minimal_ui and green_energy:
            columns = ["Provider", "CPU Cores", "RAM", "GPU", "Location", "Green Energy", "Price (€/h)"]
        else:
            columns = ["ID", "Provider", "CPU Cores", "RAM", "GPU", "Location", "Green Energy", "Price (€/h)"]

        for column in columns:
            table.add_column(column)

        for flavor in flavors:
            gpu_data = "0"
            if flavor.gpu.no > 0:
                gpu_data = str(flavor.gpu.no) + " x " + flavor.gpu.gpus[0].name + " (" + str(flavor.gpu.memory.size) + " GB)"


            if minimal_ui and not green_energy:
                table.add_row(
                    str(flavor.provider.name.value),
                    str(flavor.cpu.cores),
                    str(flavor.ram.size),
                    gpu_data,
                    str(flavor.region.location.value),
                    str(float(flavor.price.euro_price))
                )
            elif minimal_ui and green_energy:
                table.add_row(
                    str(flavor.provider.name.value),
                    str(flavor.cpu.cores),
                    str(flavor.ram.size),
                    gpu_data,
                    str(flavor.region.location.value),
                    str(bool(flavor.region.sustainable)),
                    str(float(flavor.price.euro_price))
                )
            else: table.add_row(
                flavor.pid,
                str(flavor.provider.name.value),
                str(flavor.cpu.cores),
                str(flavor.ram.size),
                gpu_data,
                str(flavor.region.location.value),
                str(bool(flavor.region.sustainable)),
                str(float(flavor.price.euro_price))
            )

        console = Console()
        console.print(table)
    else:
        app.log.warning("No matching flavors found")


class InstanceTypes(Controller):
    class Meta:
        label = 'instance-types'
        stacked_on = 'base'
        stacked_type = 'nested'

        # text displayed at the top of --help output
        description = 'Display and select vm flavors'

    @ex(
        help='get flavors on the Perian platform',
        arguments=[
            (['-f', '--filters'],
             {'help': 'Filter criteria to select flavors. A json string is expected here. Use the following command to read the filters from a .json file: "$(cat filter.json)"',
              'action': 'store'}),
            (['-c', '--cores'],
             {'help': 'Amount of cpu cores',
              'action': 'store'}),
            (['-m', '--memory'],
             {'help': 'Amount of RAM memory',
              'action': 'store'}),
            (['-g', '--gpu'],
             {'help': 'Number of GPUs',
              'action': 'store'}),
            (['-at', '--accelerator-type'],
             {'help': 'Type of accelerator',
              'action': 'store'}),
            (['-ge', '--green-energy'],
             {'help': 'Only select flavors which are powered with green energy (sustainable energy)',
              'action': 'store_true'}),
            (['-p', '--provider'],
             {'help': 'Only select flavors from specific cloud provider',
              'action': 'store'}),
            (['-t', '--token'],
             {'help': 'API token',
              'action': 'store'}),
            (['-l', '--limit'],
             {'help': 'limit the number of flavors',
              'action': 'store'})
        ],
    )
    def get(self):
        filters = self.app.pargs.filters
        token = self.app.pargs.token
        limit = self.app.pargs.limit
        only_green_energy = self.app.pargs.green_energy
        accelerator_type = self.app.pargs.accelerator_type
        provider = self.app.pargs.provider

        stored_token = self.app.db.get("token")
        endpoint = self.app.db.get("endpoint")
        stored_limit = self.app.db.get("limit")
        stored_minimal_ui = self.app.db.get("minimal_ui")

        current_token = None

        if not endpoint:
            self.app.log.error("Endpoint not configured yet. Please set the endpoint via the 'config' command")
            sys.exit(1)

        if not token and not stored_token:
            self.app.log.error("No token provided or configured. Please provided the token (--token) or configure it via the 'config' command")
            sys.exit(1)


        if not limit and not stored_limit:
            limit = 10
        elif not limit and stored_limit:
            limit = stored_limit

        if token:
            current_token = token
        elif stored_token:
            current_token = stored_token

        try:
            filter_criteria = None
            serializable_matches = [".json"]

            # check if provided filters is a json file
            if filters:
                if any([x in filters for x in serializable_matches]):
                    full_path = os.path.join(os.path.dirname(__file__), filters)

                    possible_file_paths = [filters, full_path]

                    for path in possible_file_paths:
                        if os.path.isfile(path):
                            f = open(path)
                            filter_criteria = json.load(f)

                    if not filter_criteria:
                        self.app.log.error("Provided filters file could not be found.")
                        sys.exit(1)

                # filters could be a json serializable string
                else:
                    filter_criteria = json.loads(filters)
            else:
                # no filters file provided, checking direct filter arguments
                filter_criteria = {}
                if self.app.pargs.cores:
                    filter_criteria['cpu'] = {
                        "cores": int(self.app.pargs.cores)
                    }
                if self.app.pargs.memory:
                    filter_criteria['ram'] = {
                        "size": int(self.app.pargs.memory)
                    }
                if self.app.pargs.gpu:
                    filter_criteria['gpu'] = {
                        "no": int(self.app.pargs.gpu)
                    }

                if len(filter_criteria) == 0:
                    self.app.log.error("You must either specify a json file with criteria or directly provide the filter criteria via the command line options")
                    sys.exit(1)

            # adding only sustainable flavors option
            if only_green_energy:
                filter_criteria['region'] = {
                    "sustainable": True
                }

            if provider:
                try:
                    if provider == "exo":
                        provider = "Exoscale"
                    if provider == "dc":
                        provider = "Data Crunch"
                    if provider == "gcp":
                        provider = "Google Cloud Platform"
                    if provider == "gs":
                        provider = "Gridscale"
                    if provider == "otc":
                        provider = "Open Telekom Cloud"
                    if provider == "tg":
                        provider = "Taiga Cloud"
                    if provider == "ovh":
                        provider = "OVH Cloud"

                    provider = ProviderName(provider)
                    filter_criteria['provider'] = {
                        "name": provider.value
                    }
                except Exception as e:
                    self.app.log.error("The selected cloud provider is not supported")

            if accelerator_type:
                filter_criteria['gpu'] = {
                    **filter_criteria['gpu'],
                    "name": accelerator_type
                }


        except Exception as e:
            self.app.log.error("Provided filter criteria could not be parsed")
            self.app.log.warning('Please provide either json serializable data, the path to a json file or directly enter criteria.')
            self.app.log.warning('You can read data directly from a .json file with the following command: "$(cat filters.json)"')
            sys.exit(1)

        try:
            query = perian.FlavorQuery(**filter_criteria)
            configuration = perian.Configuration(
                host=endpoint
            )

            with perian.ApiClient(configuration) as api_client:
                api_instance = perian.SelectionApi(api_client)

                try:
                    api_response = api_instance.get_flavors_selection_get_flavors_post(query, limit=int(limit), authorization="Bearer" + current_token)
                    print_flavor_results(api_response.flavors, self.app, minimal_ui=stored_minimal_ui, green_energy=only_green_energy)
                except perian.ApiException as e:
                    self.app.log.error("API error, please try again")
                    sys.exit(1)


        except Exception as e:
            self.app.log.error(e)
            sys.exit(1)



