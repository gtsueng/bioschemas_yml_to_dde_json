#### These are reusable object definitions for the most commonly expected schema.org types used in bioschemas
## Since marginality is set by bioschemas and not schema.org, 
## many of them will not have a minimal set of required properties placed under `required`.
## Instead, a minimal number of property definitions will be listed (but not required),
## With the understanding that extensive nesting and referencing may cause issues in rendering by the DDE

expected_type_dict = {
    "schema:Text": {"type": "string"},
    "schema:Integer": {"type": "integer"},
    "schema:Number": {"type": "number"},
    "schema:Boolean": {"type": "boolean"},
    "schema:Date": {"type": "string", "format":"date"},
    "schema:Datetime": {"type": "string", "format":"datetime"},
    "schema:URL": {"type": "string", "format":"uri"}
}


reusable_definitions= {
  "propertyvalue": {
    "@type": "PropertyValue",
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "value": {
        "oneOf": [
          {"type": "string"},
          {"type": "boolean"},
          {"type": "number"}
        ]
      },
      "identifier": {
        "type": "string"
      },
      "valuereference": {
        "oneOf": [
          {
            "$ref": "#/definitions/categorycode"
          },
          {
            "type": "array",
            "items": [
              {
                "$ref": "#/definitions/categorycode"
              }    
            ]
          }
        ]  
      },
      "unitCode": {
        "oneOf": [
          {
            "type": "string"},
          {
            "type": "string",
            "format": "uri"
          }
        ]      
      },
      "unitText": {
        "type": "string"
      }
    },
    "required": [
      "name",
      "value"
    ],
    "recommended": [
      "valueReference"    
    ],
    "optional": [
      "unitCode",
      "unitText"
    ]
  },
  "creativework": {
    "@type": "CreativeWork",
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "identifier": {
        "type": "string"
      },
      "url": {
        "type": "string",
        "format": "uri"
      }
    },
    "required": []
  },
  "categorycode": {
    "@type": "CategoryCode",
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "codeValue": {
        "type": "string"
      },
      "url": {
        "type": "string"
      }
    },
    "required": [
      "name",
      "codeValue",
      "url"
    ]
  },
  "taxon": {
    "@type": "bioschemas:Taxon",
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "taxonRank": {
        "anyOf": [
          {
            "$ref": "#/definitions/propertyvalue"
          },
          {
            "type": "array",
            "items": {
              "$ref": "#/definitions/propertyvalue"
            }
          },
          {
            "type": "string"
          },
          {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          {
            "type": "string",
            "format": "uri"
          },
          {
            "type": "array",
            "items": {
              "type": "string",
              "format": "uri"
            }
          }
        ]
      }
    },
    "required": [
      "name",
      "taxonRank"
    ]   
    },
  "definedterm": {
    "@type": "DefinedTerm",
    "type": "object",
    "properties": {
      "url": {
        "type": "string",
        "format": "uri"
      },
      "name": {
        "type": "string"    
      },
      "termCode": {
        "type": "string"
      },
      "identifier": {
        "type": "string"    
      },
      "inDefinedTermSet": {
        "$ref": "#/definitions/definedtermset"
      }
    },
    "required": [
    ]  
  },
  "definedtermset": {
    "@type": "DefinedTermSet",
    "type": "object",
    "properties": {
      "name": {
        "type": "string"  
      },
      "identifier": {
        "type": "string"  
      },
      "url": {
        "type": "string",
        "format": "uri"
      }
    },
    "required": []
  },
  "medicalcondition": {
    "@type": "MedicalCondition",
    "type": "object",
    "properties": {
      "url": {
        "type": "string",
        "format": "uri"
      },
      "name": {
        "type": "string"    
      },
      "identifier": {
        "type": "string"    
      }
    },
    "required": [
    ]  
  },
  "biochementity" : {
    "@type": "bioschemas:BioChemEntity",
    "type": "object",
    "properties": {
      "url": {
        "type": "string",
        "format": "uri"
      },
      "name": {
        "type": "string"    
      },
      "identifier": {
        "type": "string"    
      }
    },
    "required": [
    ]  
  },
  "gene" : {
    "@type": "bioschemas:Gene",
    "type": "object",
    "properties": {
      "identifier": {
        "anyOf": [
          {
            "$ref": "#/definitions/propertyvalue"
          },
          {
            "type": "string"
          },
          {
            "type": "string",
            "format": "uri"
          }
        ]
      },
      "name": {
        "type": "string"    
      }
    },
    "required": [
    ]  
  },
  "imageobject": {
    "@type": "ImageObject",
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "url": {
        "type": "string",
        "format": "uri"
      }
    },
    "required": []     
  },
  "person": {
    "@type": "Person",
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "url": {
        "type": "string",
        "format": "uri"
      },
      "affiliation": {
        "$ref": "#/definitions/organization"
      }
    },
    "required": [
      "name"
    ]
  },
  "organization": {
    "@type": "Organization",
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "alternateName": {
        "type": "string"
      },
      "identifier": {
        "type": "string"
      },
      "url": {
        "type": "string",
        "format": "uri"
      }
    }
  },
  "place": {
    "@type": "Place",
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "address": {
        "oneOf": [
          {"type": "string"},
          {"$ref": "#/definitions/postaladdress"}
        ]
      },
      "identifier": {
        "type": "string"
      },
      "url": {
        "type": "string",
        "format": "uri"
      }
    }
  },
  "postaladdress": {
    "@type": "PostalAddress",
    "type": "object",
    "properties": {
      "addressCountry": {
        "type": "string"  
      },
      "addressLocality": {
        "type": "string"  
      },
      "addressRegion": {
        "type": "string"  
      },
      "postOfficeBoxNumber": {
        "type": "string"  
      },
      "postalCode": {
        "type": "string"  
      },
      "streetAddress": {
        "type": "string"  
      }
    }
  }
}