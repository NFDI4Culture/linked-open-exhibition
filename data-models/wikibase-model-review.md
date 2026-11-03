| type | key | label_en | label_de | datatype | used_on | wikidata | cidoc | linked_art | lido |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| class | artwork | artwork | Kunstwerk |  |  | Q838948 | E22_Human-Made_Object | HumanMadeObject | lido:category = Man-made object |
| class | person | person | Person |  |  | Q5 | E21_Person | Person | lido:actorType = person |
| class | exhibition | exhibition | Ausstellung |  |  | Q464980 | E7_Activity | Activity | lido:eventType = Exhibition (lido00045) |
| class | exhibition_item | exhibition item | Ausstellungsobjekt |  |  | None | E7_Activity (part of the exhibition, P16_used_specific_object) | Activity (part_of exhibition, used_specific_object) | lido:eventObject within the exhibition event |
| class | material | material | Material |  |  | Q214609 | E57_Material | Material | lido:termMaterialsTech |
| class | object_type | object type | Objekttyp |  |  | Q151885 | E55_Type | Type | lido:objectWorkType |
| class | place | place | Ort |  |  | Q17334923 | E53_Place | Place | lido:placeID |
| property | equivalent_property | equivalent property | äquivalente Eigenschaft | url | property; class |  |  |  |  |
| property | local_id | local ID | lokale ID | external-id | artwork; person; exhibition; exhibition_item; material; object_type; place |  | P1_is_identified_by (E42_Identifier) | identified_by (Identifier) | lido:lidoRecID |
| property | instance_of | Type | Instanz von (Haupt-) | wikibase-item | artwork; person; exhibition; exhibition_item; material; object_type; place | P31 | P2_has_type | classified_as | lido:category / lido:objectWorkType |
| property | object_type | Artwork type | Objekttyp (Art des Kunstwerks) | wikibase-item | artwork | P31 (narrower instance of) | P2_has_type (E55_Type) | classified_as | lido:objectWorkType |
| property | title | Title | Titel | monolingualtext | artwork; exhibition | P1476 | P102_has_title (E35_Title) | identified_by (Name, classified_as title) | lido:titleWrap/lido:titleSet/lido:appellationValue |
| property | creator | Creator | Urheber/in | wikibase-item | artwork | P170 | P108i_was_produced_by > E12_Production > P14_carried_out_by | produced_by.carried_out_by | lido:eventSet (Production)/lido:eventActor |
| property | inception | Date of creation | Entstehungsdatum | time | artwork | P571 | P108i_was_produced_by > E12_Production > P4_has_time-span | produced_by.timespan | lido:eventSet (Production)/lido:eventDate |
| property | main_subject | Subject | Hauptthema | wikibase-item | artwork | P921 | P129_is_about (E1_CRM_Entity) | subject_of | lido:subjectWrap/lido:subjectSet/lido:subject |
| property | materials | Materials | Materialien | wikibase-item | artwork | P186 | P45_consists_of (E57_Material) | made_of | lido:eventMaterialsTech/lido:materialsTech |
| property | made_from_material | Material | Material | wikibase-item | artwork | P186 | P45_consists_of (E57_Material) | made_of | lido:eventMaterialsTech/lido:materialsTech |
| property | height | Height | Höhe | quantity | artwork | P2048 | P43_has_dimension (E54_Dimension, type height) | dimension (classified_as height) | lido:objectMeasurementsSet (measurementType height) |
| property | width | Width | Breite | quantity | artwork | P2049 | P43_has_dimension (E54_Dimension, type width) | dimension (classified_as width) | lido:objectMeasurementsSet (measurementType width) |
| property | depth | Depth | Tiefe | quantity | artwork | P5524 | P43_has_dimension (E54_Dimension, type depth) | dimension (classified_as depth) | lido:objectMeasurementsSet (measurementType depth) |
| property | inventory_number | Inventory no. | Inventarnummer | string | artwork | P217 | P1_is_identified_by (E42_Identifier, type inventory number) | identified_by (Identifier, classified_as inventory number) | lido:repositorySet/lido:workID |
| property | catalog_code | Catalogue no. | Katalognummer | string | artwork | P528 | P1_is_identified_by (E42_Identifier) | identified_by (Identifier) | lido:workID |
| property | image_url | Image | Bild | url | artwork | P6500 | P138i_has_representation (E36_Visual_Item) | representation (VisualItem, digitally_shown_by) | lido:resourceWrap/lido:resourceSet/lido:resourceRepresentation/lido:linkResource |
| property | part_of_series | Series | Teile einer Serie | wikibase-item | artwork | P179 | P108_has_produced (E65_Creation) | part_of_series | lido:relatedWorkSet/lido:relatedWork |
| property | depicts | Depicted motif | Darstellt | wikibase-item | artwork | P180 | P129_is_about | depicts | lido:subjectWrap/lido:subjectSet/lido:subject |
| property | iconclass | Iconclass | stellt Iconclass-Notation dar | external-id | artwork | P1257 | P62_depicts (E55_Type, Iconclass concept) | shows.represents (Type) | lido:subjectWrap/lido:subjectSet/lido:subject/lido:subjectConcept/lido:conceptID |
| property | current_owner | Owner | Aktueller Eigentümer | wikibase-item | artwork | P127 | P50_has_current_keeper | current_owner | lido:repositorySet/lido:repositoryName |
| property | commons_category | Commons category | Commons-Kategorie | url | artwork | P373 | P138i_has_representation | related | lido:resourceWrap/lido:resourceSet |
| property | wikidata_qid | Wikidata item | Wikidata-QID | external-id | artwork; person; exhibition; material; object_type; place |  | P1_is_identified_by (E42_Identifier) or owl:sameAs | equivalent | lido:objectID / lido:actorID / lido:conceptID (type wikidata) |
| property | gnd_id | GND ID | GND-ID | external-id | person | P227 | P1_is_identified_by (E42_Identifier) | equivalent / identified_by | lido:actorID (type GND) |
| property | aat_id | AAT ID | AAT-ID | external-id | material; object_type | P1014 | P1_is_identified_by (E42_Identifier) | equivalent | lido:conceptID (type AAT) |
| property | start_date | Start date | Beginn | time | exhibition | P580 | P4_has_time-span > P82a_begin_of_the_begin | timespan.begin_of_the_begin | lido:eventDate/lido:date/lido:earliestDate |
| property | end_date | End date | Ende | time | exhibition | P582 | P4_has_time-span > P82b_end_of_the_end | timespan.end_of_the_end | lido:eventDate/lido:date/lido:latestDate |
| property | exhibition | Exhibition | in Ausstellung | wikibase-item | exhibition_item | P608 | P9i_forms_part_of (E7_Activity) | part_of | lido:eventSet/lido:event (Exhibition) |
| property | exhibited_artwork | Artwork in exhibition | ausgestelltes Kunstwerk | wikibase-item | exhibition_item | P608 (inverse, stated on the artwork) | P16_used_specific_object | used_specific_object | lido:eventObject/lido:object |
| property | catalogue_number | Catalogue number | Katalognummer | string | exhibition_item | P528 | P1_is_identified_by (E42_Identifier, type catalogue number) | identified_by (Identifier, classified_as catalogue number) | lido:workID (type catalogue number) |
| property | catalogue_page | Page(s) | Seite(n) | string | exhibition_item | P304 | P3_has_note (E62_String, catalogue page) | referred_to_by (LinguisticObject, classified_as page) | lido:relatedWorkSet/lido:relatedWork |
| property | title_as_exhibited | Title as exhibited | Titel in der Ausstellung | string | exhibition_item |  | P1_is_identified_by (E35_Title) on the showing | identified_by (Name) on the part activity | lido:titleSet (type exhibited as) |
| property | note | Note | Anmerkung | string | exhibition_item |  | P3_has_note | referred_to_by (LinguisticObject) | lido:descriptiveNoteValue |
