# Artwork model review

## Main review table

| key | label_en | label_de | datatype | wikidata | cidoc | linked_art | lido | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| local_id | local ID | lokale ID | external-id |  | P1_is_identified_by (E42_Identifier) | identified_by (Identifier) | lido:lidoRecID | ok |
| instance_of | Instance of (main) | Instanz von (Haupt-) | wikibase-item | P31 | P2_has_type | classified_as | lido:category / lido:objectWorkType | ok |
| object_type | Object type (type of artwork) | Objekttyp (Art des Kunstwerks) | wikibase-item | P31 (narrower instance of); suggested Wikidata type property | P2_has_type (E55_Type) | classified_as | lido:objectWorkType | ok |
| title | Title | Titel | monolingualtext | P1476 | P102_has_title (E35_Title) | identified_by (Name, classified_as title) | lido:titleWrap/lido:titleSet/lido:appellationValue | ok |
| creator | Creator | Urheber/in | wikibase-item | P170 | P108i_was_produced_by > E12_Production > P14_carried_out_by | produced_by.carried_out_by | lido:eventSet (Production)/lido:eventActor | ok |
| inception | Date of creation | Entstehungsdatum | time | P571 | P108i_was_produced_by > E12_Production > P4_has_time-span | produced_by.timespan | lido:eventSet (Production)/lido:eventDate | ok |
| main_subject | Main Subject | Hauptthema | wikibase-item | P921, with mapping to other vocabularies optional | P129_is_about (E1_CRM_Entity) | subject_of | lido:subjectWrap/lido:subjectSet/lido:subject | ok |
| materials | Materials | Materialien | wikibase-item | P186 | P45_consists_of (E57_Material) | made_of | lido:eventMaterialsTech/lido:materialsTech | ok |
| made_from_material | made from material | Material | wikibase-item | P186 | P45_consists_of (E57_Material) | made_of | lido:eventMaterialsTech/lido:materialsTech | ok |
| height | height | Höhe | quantity | P2048 | P43_has_dimension (E54_Dimension, type height) | dimension (classified_as height) | lido:objectMeasurementsSet (measurementType height) | ok |
| width | width | Breite | quantity | P2049 | P43_has_dimension (E54_Dimension, type width) | dimension (classified_as width) | lido:objectMeasurementsSet (measurementType width) | ok |
| depth | depth | Tiefe | quantity | P5524 | P43_has_dimension (E54_Dimension, type depth) | dimension (classified_as depth) | lido:objectMeasurementsSet (measurementType depth) | ok |
| inventory_number | Inventory Number | Inventarnummer | string | P217 | P1_is_identified_by (E42_Identifier, type inventory number) | identified_by (Identifier, classified_as inventory number) | lido:repositorySet/lido:workID | ok |
| catalog_code | Catalog Code | Katalognummer | string | P528 | P1_is_identified_by (E42_Identifier) | identified_by (Identifier) | lido:workID | ok |
| location | location | Standort | wikibase-item | P276 | P55_has_current_location (E53_Place) | current_location | lido:repositorySet/lido:repositoryLocation | review |
| image_url | Image | Bild | url | P6500 (Commons URL) | P138i_has_representation (E36_Visual_Item) | representation (VisualItem, digitally_shown_by) | lido:resourceWrap/lido:resourceSet/lido:resourceRepresentation/lido:linkResource | ok |
| part_of_series | Part of Series | Teile einer Serie | wikibase-item | P179 | P108_has_produced (E65_Creation) | part_of_series | lido:relatedWorkSet/lido:relatedWork | ok |
| depicts | Depicts | Darstellt | wikibase-item | P180 | P129_is_about | depicts | lido:subjectWrap/lido:subjectSet/lido:subject | ok |
| iconclass | depicts Iconclass notation | stellt Iconclass-Notation dar | external-id | P1257, mapped alongside Wikidata subject vocabularies | P62_depicts (E55_Type, Iconclass concept) | shows.represents (Type) | lido:subjectWrap/lido:subjectSet/lido:subject/lido:subjectConcept/lido:conceptID | ok |
| current_owner | Current Owner | Aktueller Eigentümer | wikibase-item | P127; can be person, institution, or organization | P50_has_current_keeper | current_owner | lido:repositorySet/lido:repositoryName | ok |
| commons_category | Commons category | Commons-Kategorie | url | P373 | P138i_has_representation | related | lido:resourceWrap/lido:resourceSet | ok |
| wikidata_qid | Wikidata QID | Wikidata-QID | external-id |  | P1_is_identified_by (E42_Identifier) or owl:sameAs | equivalent | lido:objectID / lido:actorID / lido:conceptID (type wikidata) | ok |

## Example needs-review list

| issue | example | why it needs review |
| --- | --- | --- |
| subject vocab | Main Subject / Depicts / Iconclass | primary subject vocabulary is Wikidata, with cross-mapping to other vocabularies such as Iconclass and Getty where needed |
| material mapping | Materials / made from material | material field is confirmed as valid; multiple material statements are handled as one field in the source CSV |
| image handling | Image | confirmed as a direct URL from Commons, not a separate image entity |
| object type | Object type (type of artwork) | use a Wikidata-backed type property for painting, sculpture, print, etc., while keeping the instance-of concept distinct |
| current ownership | Current Owner | ownership may be a person, institution, or organization; the exact target item type can vary |
| location | location | confirm whether this is current collection location or exhibition venue |

> Review decisions confirmed: Materials is the canonical field; the image is a Commons URL; subject vocab is primarily Wikidata with optional mapping to other vocabularies; artwork type uses a Wikidata-backed property; ownership can be represented by different entity types.
