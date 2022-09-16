## Bioschemas yml to DDE JSON repository

### Original Intent
This repository was initially used to convert Bioschemas website yml files in to JSON-LD for inclusion in the DDE. The conversion was meant to be a rough conversion to get things started and would require manual checking to ensure compatibility of the resulting JSON LD files.

### September 2022 update
The scripts in this repository have been used to generate property and expected type frequency tables. This information will be helpful in the refactoring and improvements of the DDE as it will allow us to generate default json validation rule options. Properties from the most recent profile for each specification were aggregated to generate frequency tables. The files generated are as follows:

* [property_frequency.tsv](\results\frequency_tables\property_frequency.tsv) - The frequency of various properties and their corresponding expected types (and combinations of expected types) as they appear across different Bioschemas profiles (draft or released)

* [expected_types_frequency.tsv](\results\frequency_tables\expected_types_frequency.tsv) - The frequency of individual expected types. Combinations of expected types which may be common for a single property have been treated individually. Eg- `identifier : [Text, URL, PropertyValue]` will count once towards Text, once towards URL, and once towards PropertyValue

* [raw_expected_types_frequency.tsv](\results\frequency_tables\raw_expected_types_frequency.tsv) - The frequency of expected types and combinations of expected types irrespective of their related properties. Eg - `contributor: [Person, Organization]` will count once towards `[Person, Organization]`, while `author: [Person, Organization]` will also count once towards `[Person, Organization]`.

* [required_props.tsv](\results\frequency_tables\required_props.tsv) - This table lists all the required (ie- Marginality = Minimum) properties for the latest profile for each bioschemas specification. The required properties will be used to generate JSON schema validation rules to be used whenever a property references a bioschemas class as the expected type. For example, the Gene Profile may reference a Protein profile via a property. In this case, the Protein class would be the expected type, so the JSON schema validation rules for defining a protein object will be generated for use in the Gene Profile.

* [base_types.json](\results\frequency_tables\base_types.json) - A resulting output dictionary generated based on all individual unique expected types found across all bioschemas profiles. The resulting dictionary has the following format:
Expected Type (in lower case): corresponding JSON validation rules for that type. Eg- if the expected type of a property is `Text`, the key in this dictionary will be `text`, while the value is `{"type": "string"}`

#### Using the above information to generate default JSON schema validation rules
All properties from `property_frequency.tsv` with counts of greater than 1 (ie- it shows up in more than one profile) will have a default JSON schema validation rule created for it. Since cardinality must also be considered in the creation of the JSON schema validation rules, the python notebook contains the logic for converting a single vs multiple expected types into a JSON validation rule when only ONE vs MANY responses are acceptable. The resulting mapping files generated are as follows:

* [one_map.txt](\results\mappings\one_map.txt) - maps a hash representative of a json validation rule with a cardinality of `one` to a list of properties for which the rule applies. Eg- `jsontextrulehash` : `['name','description']` 

* [many_map.txt](\results\mappings\many_map.txt) - maps a hash representative of a json validation rule with a cardinality of `many` to a list of properties for which the rule applies. Eg- `jsonmanytextrulehash` : `['name','description']`

* [one_prop_map.txt](\results\mappings\one_prop_map.txt) - Maps each property to the appropriate hash that's representative of a json validation rule with a cardinality of `one`. Eg- `name`: `jsontextrulehash`, `description`: `jsontextrulehash` 

* [many_prop_map.txt](\results\mappings\many_prop_map.txt) - Maps each property to the appropriate hash that's representative of a json validation rule with a cardinality of `many`. Eg- `name`: `jsonmanytextrulehash`, `description`: `jsonmanytextrulehash` 

* [one_rule_map.txt](\results\mappings\one_rule_map.txt) - maps a single hash representative of a json validation rule to that json validation rule with a cardinality of `one`. Eg- `jsontextrulehash`: `{"type": "string"}`

* [many_rule_map.txt](\results\mappings\many_rule_map.txt) - maps a single hash representative of a json validation rule to that json validation rule with a cardinality of `one`. Eg- `jsonmanytextrulehash`: `{"oneOf": [{"type": "string"},{"type":"array","items":[{"type":"string"}]}]}`

* [one_prop_rule.txt](\results\mappings\one_prop_rule.txt) - maps each property to the appropriate json validation rule with a cardinality of `one`: Eg- `name` : `{"type": "string"}`

* [many_prop_rule.txt](\results\mappings\many_prop_rule.txt) - maps each property to the appropriate json validation rule with a cardinality of `many`: Eg- `name` : `{"oneOf": [{"type": "string"},{"type":"array","items":[{"type":"string"}]}]}`


#### Caveats
While the Bioschemas community has profiles (ie- clearer definitions for some specifications), this does not include many important, and re-used types. For example, FormalParameter is a useful profile that is well-defined. Hence, properties with an expected type of "FormalParameter" will have a clearly defined JSON schema validation rule. Similarly, the draft Person profile has been used for the creation of JSON schema validation rules which can be applied towards properties like `author` or `contributor`. Common properties which lack such definitions can readily be found in the [expected_types_frequency.tsv](\results\frequency_tables\expected_types_frequency.tsv) table and include things like: PropertyValue, DefinedTerm, etc. which should be reviewed by the Bioschemas community for consensus on the marginality and cardinality of the properties in these classes.