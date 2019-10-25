import json
import datetime
import sys

with open(sys.argv[1], "r") as read_file:
	decoded = json.load(read_file)

label = decoded['label']
category_label = decoded['category_label']
image = decoded['branding']['image_uri']
tagline = decoded['branding']['tagline']

now = datetime.datetime.now() 

if category_label == 'Models':
	category_label = 'tools'
elif category_label == 'Plug-ins':
	category_label= 'visualizations'
elif category_label == 'Applications':
  	category_label = 'applications'

listing = """
import {{ MarketplaceListing, fileURL }} from "../../src/data"
import {{ category, byLooker, connectionHubDetails }} from ".."

const listing: MarketplaceListing = {{
  id: [ UNIQUE STRING BASED ID ],
  label: {label},
  author: byLooker,
  branding: {{
	image_uri: [ fileURL("block-icons/FILENAME.png") ],
	tagline:
	  "{tagline}",
  }},
  versions: [
	{{
	  number: "1.0.0",
	  looker_version: ">=6.20.1",
	  released_at: "{now}",
	  release_notes_md: "Initial Marketplace Release",
	  project_git_uri: "[ GITHUB REPO ]",
	  project_git_ref: "[ GITHUB COMMIT REF ]",
	}},
  ],
  connection_hub_details: connectionHubDetails("Zendesk data"),
  hero_image_uris: [
	"[ IMAGE 1 ]",
	"[ IMAGE 2 ]",
  ],
  metadata_fields: [
	{{
	  id: "etl-providers",
	  label: "ETL Providers",
	  values: ["Looker", "Fivetran"],
	}},
	{{
	  id: "dialects",
	  label: "SQL Dialects",
	  values: ["Google BigQuery"],
	}},
  ],
  documentation_uri: "https://docs.looker.com/apps/coolzone",
  support_uri: "https://docs.looker.com/support/coolzone",
  description_md: `[ DESCRIPTION ]`,
  category: category("{category_label}"),
}}

export default listing 
""".format(label=label, tagline=tagline, now=now, category_label=category_label.lower())

with open("listing.ts", "w") as write_file:
	write_file.write(listing)






