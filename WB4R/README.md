## Wikibase Generic Model for Digital Objects
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/    
**authors** Lozana Rossenova, Lucia Sohmen, Paul Duchesne    
**version** 2025-07-30    
## **Classes**    
### actor    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**label_de** Akteur:in    
**label_en** Actor    
**description_de** umfasst Menschen, entweder einzeln oder in Gruppen, die das Potenzial haben, vorsätzliche Handlungen zu begehen, für die jemand zur Verantwortung gezogen werden kann    
**description_en** comprises people, either individually or in groups, who have the potential to perform intentional actions of kinds for which someone may be held responsible    
**type** http://www.w3.org/2002/07/owl#Class    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E39_CRM_Actor, http://xmlns.com/foaf/0.1/#term_Agent    
**note_en** Wikibase ID: Q1    
### annotation    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**label_de** Annotation    
**label_en** Annotation    
**description_de** Text, der an ein Medienelement oder einen anderen Text angehängt ist, um weitere Informationen zu liefern    
**description_en** text that is attached to a media item or another text to provide more information    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object    
**equivalent class** http://www.ics.forth.gr/isl/CRMdig/D29_Annotation_Object, http://www.w3.org/ns/oa#Annotation, http://www.wikidata.org/entity/Q857525    
**note_en** Wikibase ID: Q15    
### attribute_assignment    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/attribute_assignment    
**label_de** Merkmalszuweisung    
**label_en** attribute assignment    
**description_de** Ereignis bei dem ein Merkmal zugewiesen wurde    
**description_en** event where an attribute was assigned    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E13_Attribute_Assignment    
**note_en** Wikibase ID: Q97    
### bibliographic_work    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/bibliographic_work    
**label_de** Bibliografisches Werk    
**label_en** Bibliographic Work    
**description_de** Instanzen dieser Klasse können zitiert werden, um eine Behauptung zu belegen    
**description_en** instances of this class can be cited to support a claim    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object    
**equivalent class** http://iflastandards.info/ns/fr/frbr/frbroo/F19_Publication_Work, http://www.wikidata.org/entity/Q59156095    
**note_en** Wikibase ID: Q14    
### biological_object    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/biological_object    
**label_de** Biologischer Gegenstand    
**label_en** Biological Object    
**description_de** umfasst einzelne Gegenstände materieller Natur, die leben, gelebt haben oder natürliche Produkte von oder aus lebenden Organismen sind    
**description_en** comprises individual items of a material nature, which live, have lived or are natural products of or from living organisms    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**equivalent class** http://cidoc-crm.org/cidoc-crm/E20_Biological_Object    
**note_en** Wikibase ID: Q4    
### birth    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/birth    
**label_de** Geburt    
**label_en** Birth    
**description_de** ein biologisches Ereignis, das sich auf den Kontext konzentriert, in dem Menschen auf die Welt kommen    
**description_en** a biological event focussing on the context of people coming into life    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**equivalent class** http://cidoc-crm.org/cidoc-crm/7.1.2/E67_Birth    
**note_en** Wikibase ID: Q71    
### change_of_custody    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/change_of_custody    
**label_de** Besitzwechsel    
**label_en** Change of custody    
**description_de** Ereignis, bei dem der Verwahrer einer Sache wechselt    
**description_en** event where the custodian of an item changes    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E10_Transfer_of_Custody    
**note_en** Wikibase ID: Q23    
### change_of_ownership    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/change_of_ownership    
**label_de** Eigentumswechsel    
**label_en** Change of ownership    
**description_de** Ereignis, bei dem der Eigentümer einer Sache wechselt    
**description_en** event where the owner of an item changes    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E8_Acquisition    
**note_en** Wikibase ID: Q24    
### city    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/city    
**label_de** Stadt    
**label_en** city    
**description_de** Ortstyp    
**description_en** type of location    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/place    
**note_en** Wikibase ID: Q74    
### collection    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/collection    
**label_de** Sammlung    
**label_en** Collection    
**description_de** Zusammenstellung von physischen Dingen, die von einem Akteur kuratiert werden – nicht für digitale Objekte, stattdessen »digitale Sammlung« verwenden    
**description_en** aggregation of physical things that are being curated by an actor - not for digital objects, use Digital collection instead    
**type** http://www.w3.org/2002/07/owl#Class    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E78_Collection    
**note_en** Wikibase ID: Q7    
### conceptual_object    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object    
**label_de** Begrifflicher Gegenstand    
**label_en** Conceptual Object    
**description_de** umfasst nicht materielle Produkte unseres Geistes und andere von Menschen produzierte Daten    
**description_en** comprises non-material products of our minds and other human produced data    
**type** http://www.w3.org/2002/07/owl#Class    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E28_Conceptual_Object    
**note_en** Wikibase ID: Q8    
### condition    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/condition    
**label_de** Zustand    
**label_en** Condition    
**description_de** Zustand eines Gegenstands    
**description_en** condition of an object    
**type** http://www.w3.org/2002/07/owl#Class    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E3_Condition_State, http://www.wikidata.org/entity/Q813912    
**note_en** Wikibase ID: Q20    
### country    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/country    
**label_de** Land    
**label_en** Country    
**description_de** bestehendes oder ehemals bestehendes Land    
**description_en** existing or previously existing country    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/place    
**equivalent class** https://nfdi4culture.de/ontology#Country    
**note_en** Wikibase ID: Q73    
### creation    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/creation    
**label_de** Herstellung    
**label_en** Creation    
**description_de** Ereignis, das zur Erstellung eines Objekts führt    
**description_en** event that results in an item being created    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E12_Production    
**note_en** Wikibase ID: Q25    
### death    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/death    
**label_de** Tod    
**label_en** Death    
**description_de** umfasst den Tod von Menschen    
**description_en** comprises the deaths of human beings    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**equivalent class** http://cidoc-crm.org/cidoc-crm/7.1.2/E69_Death    
**note_en** Wikibase ID: Q72    
### degree_of_certainty    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/degree_of_certainty    
**label_de** Grad der Sicherheit    
**label_en** degree of certainty    
**description_de** wird für Aussagen verwendet, um den Grad der Sicherheit auszudrücken    
**description_en** used in statements for expressing the degree of certainty    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object    
**note_en** Wikibase ID: Q92    
### destruction    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/destruction    
**label_de** Zerstörung    
**label_en** Destruction    
**description_de** Ereignis, das dazu führt, dass ein Objekt nicht mehr existiert    
**description_en** event that results in an item no longer existing    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E6_Destruction    
**note_en** Wikibase ID: Q26    
### digital_collection    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/digital_collection    
**label_de** Digitale Sammlung    
**label_en** Digital Collection    
**description_de** Gruppierung digitaler Gegenstände    
**description_en** aggregation of digital objects    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/information_object    
**equivalent class** http://www.wikidata.org/entity/Q60474998    
**note_en** Wikibase ID: Q10    
### digital_object    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/digital_object    
**label_de** Digitales Objekt    
**label_en** Digital Object    
**description_de** umfasst identifizierbare immaterielle Güter, die als Mengen von Bitfolgen dargestellt werden können, wie Datensätze, elektronische Texte, Bilder, Audio- oder Videoelemente, Software usw., und die als einzelne Einheiten dokumentiert werden    
**description_en** comprises identifiable immaterial items that can be represented as sets of bit sequences, such as data sets, e-texts, images, audio or video items, software, etc., and are documented as single units    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/information_object    
**equivalent class** http://www.ics.forth.gr/isl/CRMdig/D1_Digital_Object, http://www.wikidata.org/entity/Q59138870    
**note_en** Wikibase ID: Q11    
### digitization    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/digitization    
**label_de** Digitalisierung    
**label_en** Digitization    
**description_de** Ereignis, das zu einer neuen digitalen Objektdarstellung eines Gegenstands führt    
**description_en** event that results in a new digital object representation of an item    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/creation    
**equivalent class** http://www.ics.forth.gr/isl/CRMdig/D2_Digitization_Process    
**note_en** Wikibase ID: Q27    
### event    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**label_de** Ereignis    
**label_en** Event    
**description_de** Oberklasse für Ereignisse    
**description_en** superclass for events    
**type** http://www.w3.org/2002/07/owl#Class    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E5_Event    
**note_en** Wikibase ID: Q22    
### file_format    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/file_format    
**label_de** Datenformat    
**label_en** File Format    
**description_de** Kodierungsformat einer digitalen Datei    
**description_en** encoding format of a digital file    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/digital_object    
**equivalent class** http://purl.org/dc/terms/FileFormat    
**note_en** Wikibase ID: Q39    
### function    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/function    
**label_de** Funktion    
**label_en** Function    
**description_de** beschreibt die Verwendung eines Objekts    
**description_en** describes the use of an item    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/type    
**note_en** Wikibase ID: Q40    
### group    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/group    
**label_de** Menschliche Gruppe    
**label_en** Group    
**description_de** alle Ansammlungen oder Organisationen menschlicher Individuen oder Gruppen, die aufgrund irgendeiner Form von verbindenden Beziehungen kollektiv oder in ähnlicher Weise handeln    
**description_en** any gatherings or organizations of human individuals or groups that act collectively or in a similar way due to any form of unifying relationship    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E74_Group, http://www.wikidata.org/entity/Q16887380, http://xmlns.com/foaf/0.1/#term_Group    
**note_en** Wikibase ID: Q2    
### human    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/human    
**label_de** Mensch    
**label_en** Human    
**description_de** (realer) toter oder lebender Mensch    
**description_en** (real) dead or living human being    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/actor, https://gitlab.com/nfdi4culture/wikibase4research/model/biological_object    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E21_Person, http://www.wikidata.org/entity/Q5, http://xmlns.com/foaf/0.1/#term_Person, https://schema.org/Person    
**note_en** Wikibase ID: Q5    
### human-made_object    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/human-made_object    
**label_de** Menschengemachter Gegenstand    
**label_en** Human-Made Object    
**description_de** alle dauerhaften physischen Gegenstände jeglicher Größe, die absichtlich durch menschliche Aktivitäten geschaffen werden    
**description_en** all persistent physical objects of any size that are purposely created by human activity    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E22_Human-Made_Object, http://www.wikidata.org/entity/Q223557    
**note_en** Wikibase ID: Q6    
### iconographic_concept    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/iconographic_concept    
**label_de** Ikonografisches Konzept    
**label_en** Iconographic Concept    
**description_de** etwas, das auf einem Gegenstand abgebildet werden kann    
**description_en** something that can be depicted on an object    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/type    
**note_en** Wikibase ID: Q43    
### information_object    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/information_object    
**label_de** Informationsgegenstand    
**label_en** Information Object    
**description_de** umfasst identifizierbare immaterielle Güter wie Datensätze, Bilder, Texte, Multimedia-Objekte, Computercode, Algorithmen oder mathematische Formeln, die eine objektiv erkennbare Struktur aufweisen und als einzelne Einheiten dokumentiert sind    
**description_en** comprises identifiable immaterial items, such as data sets, images, texts, multimedia objects, computer code, algorithm or mathematical formulae, that have an objectively recognizable structure and are documented as single units    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object    
**equivalent class** http://cidoc-crm.org/cidoc-crm/E73_Information_Object    
**note_en** Wikibase ID: Q9    
### licence    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/licence    
**label_de** Lizenz    
**label_en** Licence    
**description_de** Art der Nutzungsrechte    
**description_en** type of usage right    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/information_object    
**equivalent class** http://www.ebi.ac.uk/swo/SWO_0000002    
**note_en** Wikibase ID: Q37    
### material    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/material    
**label_de** Material    
**label_en** Material    
**description_de** Material, aus dem ein Gegenstand hergestellt ist    
**description_en** material that an object is made from    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/type    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E57_Material, http://www.wikidata.org/entity/Q214609, https://schema.org/material    
**note_en** Wikibase ID: Q18    
### measurement_unit    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**label_de** Maßeinheit    
**label_en** Measurement Unit    
**description_de** Einheit zur Angabe eines Maßes, z. B. Meter oder Liter    
**description_en** unit for giving a measurement, for example metres or litres    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/type    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E58_Measurement_Unit, http://www.wikidata.org/entity/Q47574    
**note_en** Wikibase ID: Q19    
### media_item    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/media_item    
**label_de** Medienelement    
**label_en** Media item    
**description_de** digitale Darstellung von Medien, etwa Video oder Audio    
**description_en** digital representation of media, for example video or audio    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/digital_object    
**equivalent class** https://schema.org/MediaObject    
**note_en** Wikibase ID: Q12    
### modification    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/modification    
**label_de** Bearbeitung    
**label_en** Modification    
**description_de** Ereignis, bei dem sich ein Objekt ändert, aber immer noch als dasselbe Objekt betrachtet wird (spezifischere Ereignisse können Teil Hinzufügen und Teil Entfernen sein)    
**description_en** event where an item changes but is still considered the same item (more specific events can be part addition and part removal)    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E11_Modification    
**note_en** Wikibase ID: Q28    
### motivation    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/motivation    
**label_de** Motivation    
**label_en** Motivation    
**description_de** für Anmerkungen zu verwenden    
**description_en** to be used for annotations    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object    
**equivalent class** http://www.w3.org/ns/oa#Motivation, http://www.wikidata.org/entity/Q644302    
**note_en** Wikibase ID: Q16    
### move    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/move    
**label_de** Ortswechsel    
**label_en** Move    
**description_de** Ereignis, bei dem ein Objekt von einem Ort zu einem anderen bewegt wird    
**description_en** event where an item is moved from one place to another    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E9_Move    
**note_en** Wikibase ID: Q29    
### organization    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/organization    
**label_de** Organisation    
**label_en** Organization    
**description_de** eine organisierte Gruppe von Menschen, z. B. eine Universität oder eine Forschungsgesellschaft    
**description_en** organized group of humans such as a university or research society    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**equivalent class** http://www.wikidata.org/entity/Q43229, http://xmlns.com/foaf/0.1/#term_Organization, https://nfdi4culture.de/ontology#Organization, https://schema.org/Organization    
**note_en** Wikibase ID: Q35    
### part_addition    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/part_addition    
**label_de** Teilhinzufügung    
**label_en** Part Addition    
**description_de** Ereignis, bei dem ein Teil zu einem Objekt hinzugefügt wird    
**description_en** event where a part gets added to an item    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E79_Part_Addition    
**note_en** Wikibase ID: Q30    
### part_removal    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/part_removal    
**label_de** Teilentfernung    
**label_en** Part Removal    
**description_de** Ereignis, bei dem ein Teil von einem Objekt entfernt wird    
**description_en** event where a part is removed from an item    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E80_Part_Removal    
**note_en** Wikibase ID: Q31    
### physical_object    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**label_de** Materieller Gegenstand    
**label_en** Physical Object    
**description_de** umfasst Gegenstände materieller Art, die Dokumentationseinheiten sind und physische Grenzen haben, die sie auf objektive Weise vollständig von anderen Gegenständen trennen    
**description_en** comprises items of a material nature that are units for documentation and have physical boundaries that separate them completely in an objective way from other objects    
**type** http://www.w3.org/2002/07/owl#Class    
**equivalent class** http://cidoc-crm.org/cidoc-crm/E19_Physical_Object    
**note_en** Wikibase ID: Q3    
### place    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/place    
**label_de** Ort    
**label_en** Place    
**description_de** jede Art von Standort    
**description_en** any kind of location    
**type** http://www.w3.org/2002/07/owl#Class    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E53_Place, http://www.wikidata.org/entity/Q2221906, https://nfdi4culture.de/ontology#Place, https://schema.org/Place    
**note_en** Wikibase ID: Q21    
### position    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/position    
**label_de** Position    
**label_en** Position    
**description_de** Position eines Objekts innerhalb eines Standorts (etwa an der Wand oder Decke)    
**description_en** position of an item within a location (for example wall or ceiling)    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/type    
**note_en** Wikibase ID: Q41    
### primitive_value    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/primitive_value    
**label_de** Primitiver Wert    
**label_en** Primitive Value    
**description_de** umfasst Werte von primitiven Datentypen von Programmiersprachen oder Datenbankverwaltungssystemen und aus solchen Werten zusammengesetzte Datentypen, die als Dokumentationselemente verwendet werden, sowie deren mathematische Abstraktionen    
**description_en** comprises values of primitive data types of programming languages or database management systems and data types composed of such values used as documentation elements, as well as their mathematical abstractions    
**type** http://www.w3.org/2002/07/owl#Class    
**equivalent class** http://cidoc-crm.org/cidoc-crm/7.1.2/E59_Primitive_Value    
**note_en** Wikibase ID: Q34    
### raw_data_creation    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/raw_data_creation    
**label_de** Rohdatenerzeugung    
**label_en** Raw data creation    
**description_de** Ereignis, das zur Erstellung der Rohdaten eines Objekts führt    
**description_en** event that results in the raw data for an item being created    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/creation    
**note_en** Wikibase ID: Q32    
### sex_or_gender    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/sex_or_gender    
**label_de** Geschlecht oder Geschlechtsidentität    
**label_en** Sex or gender    
**description_de** für Menschen zu verwenden    
**description_en** to be used for humans    
**type** http://www.w3.org/2002/07/owl#Class    
**equivalent class** http://purl.obolibrary.org/obo/NCIT_C28421, http://www.wikidata.org/entity/Q18382802    
**note_en** Wikibase ID: Q36    
### software    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/software    
**label_de** Software    
**label_en** Software    
**description_de** für die Erstellung von Medienelementen verwendete Software    
**description_en** software used for creation of media item    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/digital_object    
**equivalent class** http://www.ics.forth.gr/isl/CRMdig/D14_Software, http://www.wikidata.org/entity/Q7397, https://schema.org/SoftwareApplication    
**note_en** Wikibase ID: Q13    
### style    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/style    
**label_de** Stil    
**label_en** Style    
**description_de** Stil eines Kulturguts    
**description_en** style of a cultural heritage object    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/type    
**note_en** Wikibase ID: Q42    
### technique    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/technique    
**label_de** Verfahren    
**label_en** Technique    
**description_de** Technik oder Methode, die zur Erstellung oder Änderung eines Gegenstands verwendet wird    
**description_en** technique or method that is used for creating or changing an object    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/type    
**equivalent class** http://www.wikidata.org/entity/Q2695280    
**note_en** Wikibase ID: Q38    
### transformation    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/transformation    
**label_de** Umwandlung    
**label_en** Transformation    
**description_de** Ereignis, bei dem ein Objekt so stark verändert wird, dass es nicht mehr als dasselbe Objekt angesehen werden kann - das Ergebnis ist ein neues Objekt    
**description_en** event where one item is changed so significantly it can no longer be considered the same item - the result is a new item    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E81_Transformation    
**note_en** Wikibase ID: Q33    
### type    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/type    
**label_de** Typus    
**label_en** Type    
**description_de** umfasst Konzepte, die durch Begriffe aus Thesauri und kontrollierten Vokabularien bezeichnet werden, die zur Charakterisierung und Klassifizierung von Instanzen der Kernklassen der Ontologie verwendet werden    
**description_en** comprises concepts denoted by terms from thesauri and controlled vocabularies used to characterize and classify instances of core ontology classes    
**type** http://www.w3.org/2002/07/owl#Class    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object    
**equivalent class** http://www.cidoc-crm.org/cidoc-crm/E55_Type    
**note_en** Wikibase ID: Q17    
## **Individuals**    
### all_rights_reserved    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/all_rights_reserved    
**label_de** Alle Rechte vorbehalten    
**label_en** All Rights Reserved    
**description_de** Rechtserklärung zu Werken, die dem Urheberrecht unterliegen    
**description_en** rights statement pertaining to works which are in copyright    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/licence    
**same as** http://www.wikidata.org/entity/Q1752207    
**note_en** Wikibase ID: Q54    
### assessing    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/assessing    
**label_de** beurteilen    
**label_en** assessing    
**description_de** wird zusammen mit P80 (Motivation) verwendet, wenn die/der Benutzende beabsichtigt, die Zielentität zu bewerten, anstatt nur eine Bemerkung über sie zu machen    
**description_en** used with P80 (motivation) for when the user intends to assess the target entity in some way, rather than simply make a comment about it    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/motivation    
**same as** http://www.w3.org/ns/oa#assessing    
**note_en** Wikibase ID: Q58    
### bookmarking    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/bookmarking    
**label_de** Lesezeichen setzen    
**label_en** bookmarking    
**description_de** wird zusammen mit P80 (Motivation) verwendet, wenn die/der Benutzende beabsichtigt, ein Lesezeichen für die Zielentität oder einen Teil davon zu setzen    
**description_en** used with P80 (motivation) for when the user intends to create a bookmark to the target entity or part thereof    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/motivation    
**same as** http://www.w3.org/ns/oa#bookmarking    
**note_en** Wikibase ID: Q59    
### byte    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/byte    
**label_de** Byte    
**label_en** byte    
**description_de** Maßeinheit    
**description_en** measurement unit    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**note_en** Wikibase ID: Q91    
### cc0    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/cc0    
**label_de** CC0    
**label_en** CC0    
**description_de** Rechtsdokument, mit dem ein urheberrechtlich geschütztes Werk der Öffentlichkeit zugänglich gemacht wird    
**description_en** legal document dedicating a copyrighted work to the public domain    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/licence    
**same as** http://www.wikidata.org/entity/Q6938433    
**note_en** Wikibase ID: Q46    
### centimetre    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/centimetre    
**label_de** Zentimeter    
**label_en** centimetre    
**description_de** Maßeinheit    
**description_en** measurement unit    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**note_en** Wikibase ID: Q76    
### classifying    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/classifying    
**label_de** klassifizieren    
**label_en** classifying    
**description_de** wird zusammen mit P80 (Motivation) verwendet, wenn die/der Benutzende beabsichtigt, die Zielentität als etwas zu klassifizieren    
**description_en** used with P80 (motivation) for when the user intends to classify the target entity as something    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/motivation    
**same as** http://www.w3.org/ns/oa#classifying    
**note_en** Wikibase ID: Q60    
### commenting    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/commenting    
**label_de** kommentieren    
**label_en** commenting    
**description_de** wird zusammen mit P80 (Motivation) verwendet, wenn die/der Benutzende beabsichtigt, einen Kommentar über die Zielentität abzugeben    
**description_en** used with P80 (motivation) for when the user intends to comment about the target entity    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/motivation    
**same as** http://www.w3.org/ns/oa#commenting    
**note_en** Wikibase ID: Q61    
### creative_commons_attribution    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/creative_commons_attribution    
**label_de** Creative Commons Namensnennung    
**label_en** Creative Commons Attribution    
**description_de** Lizenz, die die freie Nutzung Copyright geschützten Materials unter Nennung des Namens erlaubt    
**description_en** license allowing free use of a copyrighted work, with attribution    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/licence    
**same as** http://www.wikidata.org/entity/Q6905323    
**note_en** Wikibase ID: Q47    
### creative_commons_attribution-noderivatives    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/creative_commons_attribution-noderivatives    
**label_de** Creative Commons Namensnennung-KeineBearbeitung    
**label_en** Creative Commons Attribution-NoDerivatives    
**description_de** Lizenzsatz, der die Verbreitung ohne Änderungen erlaubt und die Nennung des Namens erfordert    
**description_en** set of licenses allowing distribution without modification, and requiring attribution    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/licence    
**same as** http://www.wikidata.org/entity/Q6999319    
**note_en** Wikibase ID: Q51    
### creative_commons_attribution-noncommercial    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/creative_commons_attribution-noncommercial    
**label_de** Creative Commons Namensnennung-NichtKommerziell    
**label_en** Creative Commons Attribution-NonCommercial    
**description_de** Lizenzsatz, der die nicht kommerzielle Verbreitung erlaubt und die Nennung des Namens erfordert    
**description_en** set of licenses allowing free noncommercial use, and requiring attribution    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/licence    
**same as** http://www.wikidata.org/entity/Q6936496    
**note_en** Wikibase ID: Q49    
### creative_commons_attribution-noncommercial-noderivatives    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/creative_commons_attribution-noncommercial-noderivatives    
**label_de** Creative Commons Namensnennung-NichtKommerziell-KeineBearbeitung    
**label_en** Creative Commons Attribution-NonCommercial-NoDerivatives    
**description_de** Lizenzsatz, der die nicht kommerzielle Verbreitung ohne Änderungen erlaubt und die Nennung des Namens erfordert    
**description_en** set of licenses allowing noncommercial distribution without modification, and requiring attribution    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/licence    
**same as** http://www.wikidata.org/entity/Q6937225    
**note_en** Wikibase ID: Q50    
### creative_commons_attribution-noncommercial-sharealike    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/creative_commons_attribution-noncommercial-sharealike    
**label_de** Creative Commons Namensnennung-NichtKommerziell-WeitergabeUnterGleichenBedingungen    
**label_en** Creative Commons Attribution-NonCommercial-ShareAlike    
**description_de** Lizenz, die die nicht kommerzielle Nutzung und Verbreitung unter derselben Lizenz und der Nennung des Namens erlaubt    
**description_en** license allowing noncommercial use and distribution, with attribution, under the same license    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/licence    
**same as** http://www.wikidata.org/entity/Q6998997    
**note_en** Wikibase ID: Q52    
### creative_commons_attribution-sharealike    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/creative_commons_attribution-sharealike    
**label_de** Creative Commons Namensnennung-WeitergabeUnterGleichenBedingungen    
**label_en** Creative Commons Attribution-ShareAlike    
**description_de** Lizenzsatz, der die Nutzung unter derselben Lizenz erlaubt und die Nennung des Namens erfordert    
**description_en** set of licenses allowing free use of a work, with attribution, under the same conditions    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/licence    
**same as** http://www.wikidata.org/entity/Q6905942    
**note_en** Wikibase ID: Q48    
### describing    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/describing    
**label_de** beschreiben    
**label_en** describing    
**description_de** wird zusammen mit P80 (Motivation) verwendet, wenn die/der Benutzende beabsichtigt, die Zielentität zu beschreiben    
**description_en** used with P80 (motivation) for when the user intends to describe the target entity    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/motivation    
**same as** http://www.w3.org/ns/oa#describing    
**note_en** Wikibase ID: Q62    
### editing    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/editing    
**label_de** bearbeiten    
**label_en** editing    
**description_de** wird zusammen mit P80 (Motivation) verwendet, wenn die/der Benutzende beabsichtigt, eine Änderung oder Bearbeitung der Zielentität zu beantragen    
**description_en** used with P80 (motivation) for when the user intends to request a change or edit to the target entity    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/motivation    
**same as** http://www.w3.org/ns/oa#editing    
**note_en** Wikibase ID: Q63    
### false    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/false    
**label_de** FALSE    
**label_en** FALSE    
**description_de** Wert für bestimmte Eigenschaften, wie P83 (verifiziert)    
**description_en** value for specific properties, like P83 (verified)    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object    
**equivalent class** https://schema.org/False    
**note_en** Wikibase ID: Q45    
### female    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/female    
**label_de** weiblich    
**label_en** female    
**description_de** gibt an, dass es sich bei der Person um eine Frau handelt    
**description_en** indicates that the human subject is a female    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/sex_or_gender    
**same as** https://www.wikidata.org/wiki/Q6581072    
**note_en** Wikibase ID: Q55    
### gigabyte    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/gigabyte    
**label_de** Gigabyte    
**label_en** gigabyte    
**description_de** Maßeinheit    
**description_en** measurement unit    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**note_en** Wikibase ID: Q77    
### gram    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/gram    
**label_de** Gramm    
**label_en** gram    
**description_de** Maßeinheit    
**description_en** measurement unit    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**note_en** Wikibase ID: Q78    
### high    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/high    
**label_de** hoch    
**label_en** high    
**description_de** Grad der Sicherheit einer Aussage    
**description_en** degree of certainty of a statement    
**type** http://www.w3.org/2002/07/owl#NamedIndividual    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/degree_of_certainty    
**note_en** Wikibase ID: Q93    
### highlighting    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/highlighting    
**label_de** hervorheben    
**label_en** highlighting    
**description_de** wird zusammen mit P80 (Motivation) verwendet, wenn die/der Benutzende beabsichtigt, die Zielentität oder ein Segment davon zu markieren    
**description_en** used with P80 (motivation) for when the user intends to highlight the target entity or segment of it    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/motivation    
**same as** http://www.w3.org/ns/oa#highlighting    
**note_en** Wikibase ID: Q64    
### hour    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/hour    
**label_de** Stunde    
**label_en** hour    
**description_de** Maßeinheit    
**description_en** measurement unit    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**note_en** Wikibase ID: Q79    
### identifying    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/identifying    
**label_de** identifizieren    
**label_en** identifying    
**description_de** wird zusammen mit P80 (Motivation) verwendet, wenn die/der Benutzende beabsichtigt, der Zielentität eine Identität zuzuweisen    
**description_en** used with P80 (motivation) for when the user intends to assign an identity to the target entity    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/motivation    
**same as** http://www.w3.org/ns/oa#identifying    
**note_en** Wikibase ID: Q65    
### kilogram    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/kilogram    
**label_de** Kilogramm    
**label_en** kilogram    
**description_de** Maßeinheit    
**description_en** measurement unit    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**note_en** Wikibase ID: Q80    
### kilometre    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/kilometre    
**label_de** Kilometer    
**label_en** kilometre    
**description_de** Maßeinheit    
**description_en** measurement unit    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**note_en** Wikibase ID: Q82    
### linking    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/linking    
**label_de** verlinken    
**label_en** linking    
**description_de** wird zusammen mit P80 (Motivation) verwendet, wenn die/der Benutzende beabsichtigt, einen Link zu einer Ressource zu erstellen, die mit der Zielentität in Verbindung steht    
**description_en** used with P80 (motivation) for when the user intends to link to a resource related to the target entity    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/motivation    
**same as** http://www.w3.org/ns/oa#linking    
**note_en** Wikibase ID: Q66    
### litre    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/litre    
**label_de** Liter    
**label_en** litre    
**description_de** Maßeinheit    
**description_en** measurement unit    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**note_en** Wikibase ID: Q83    
### low    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/low    
**label_de** niedrig    
**label_en** low    
**description_de** Grad der Sicherheit einer Aussage    
**description_en** degree of certainty of a statement    
**type** http://www.w3.org/2002/07/owl#NamedIndividual    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/degree_of_certainty    
**note_en** Wikibase ID: Q95    
### male    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/male    
**label_de** männlich    
**label_en** male    
**description_de** gibt an, dass es sich bei der Person um einen Mann handelt    
**description_en** indicates that the human subject is a male    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/sex_or_gender    
**same as** https://www.wikidata.org/wiki/Q6581097    
**note_en** Wikibase ID: Q56    
### metre    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/metre    
**label_de** Meter    
**label_en** metre    
**description_de** Maßeinheit    
**description_en** measurement unit    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**note_en** Wikibase ID: Q89    
### mid    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/mid    
**label_de** mittel    
**label_en** mid    
**description_de** Grad der Sicherheit einer Aussage    
**description_en** degree of certainty of a statement    
**type** http://www.w3.org/2002/07/owl#NamedIndividual    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/degree_of_certainty    
**note_en** Wikibase ID: Q94    
### milligram    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/milligram    
**label_de** Milligramm    
**label_en** milligram    
**description_de** Maßeinheit    
**description_en** measurement unit    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**note_en** Wikibase ID: Q84    
### millilitre    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/millilitre    
**label_de** Milliliter    
**label_en** millilitre    
**description_de** Maßeinheit    
**description_en** measurement unit    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**note_en** Wikibase ID: Q86    
### millimetre    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/millimetre    
**label_de** Millimeter    
**label_en** millimetre    
**description_de** Maßeinheit    
**description_en** measurement unit    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**note_en** Wikibase ID: Q87    
### minute    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/minute    
**label_de** Minute    
**label_en** minute    
**description_de** Maßeinheit    
**description_en** measurement unit    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**note_en** Wikibase ID: Q85    
### moderating    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/moderating    
**label_de** moderieren    
**label_en** moderating    
**description_de** wird zusammen mit P80 (Motivation) verwendet, wenn die/der Benutzende beabsichtigt, der Zielentität einen Wert oder eine Qualität zuzuweisen    
**description_en** used with P80 (motivation) for when the user intends to assign some value or quality to the target entity    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/motivation    
**same as** http://www.w3.org/ns/oa#moderating    
**note_en** Wikibase ID: Q67    
### non-binary    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/non-binary    
**label_de** nicht-binär    
**label_en** non-binary    
**description_de** andere Geschlechtsidentitäten als männlich oder weiblich    
**description_en** gender identities other than male or female    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/sex_or_gender    
**same as** https://www.wikidata.org/wiki/Q48270    
**note_en** Wikibase ID: Q57    
### questioning    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/questioning    
**label_de** hinterfragen    
**label_en** questioning    
**description_de** wird zusammen mit P80 (Motivation) verwendet, wenn die/der Benutzende beabsichtigt, eine Frage über die Zielentität zu stellen    
**description_en** used with P80 (motivation) for when the user intends to ask a question about the target entity    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/motivation    
**same as** http://www.w3.org/ns/oa#questioning    
**note_en** Wikibase ID: Q68    
### replying    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/replying    
**label_de** beantworten    
**label_en** replying    
**description_de** wird zusammen mit P80 (Motivation) verwendet, wenn die/der Benutzende beabsichtigt, auf eine frühere Aussage zu antworten, entweder auf eine Anmerkung oder eine andere Ressource    
**description_en** used with P80 (motivation) for when the user intends to reply to a previous statement, either an annotation or another resource    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/motivation    
**same as** http://www.w3.org/ns/oa#replying    
**note_en** Wikibase ID: Q69    
### second    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/second    
**label_de** Sekunde    
**label_en** second    
**description_de** Maßeinheit    
**description_en** measurement unit    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**note_en** Wikibase ID: Q90    
### some_rights_reserved    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/some_rights_reserved    
**label_de** einige Rechte vorbehalten    
**label_en** Some rights reserved    
**description_de** Lizenz, die eine eingeschränkte Nutzung erlaubt    
**description_en** license that allows limited use    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/licence    
**same as** http://www.wikidata.org/entity/Q47530729    
**note_en** Wikibase ID: Q53    
### square_centimetre    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/square_centimetre    
**label_de** Quadratzentimeter    
**label_en** square centimetre    
**description_de** Maßeinheit    
**description_en** measurement unit    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**note_en** Wikibase ID: Q75    
### square_kilometre    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/square_kilometre    
**label_de** Quadratkilometer    
**label_en** square kilometre    
**description_de** Maßeinheit    
**description_en** measurement unit    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**note_en** Wikibase ID: Q81    
### square_metre    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/square_metre    
**label_de** Quadratmeter    
**label_en** square metre    
**description_de** Maßeinheit    
**description_en** measurement unit    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/measurement_unit    
**note_en** Wikibase ID: Q88    
### tagging    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/tagging    
**label_de** markieren    
**label_en** tagging    
**description_de** wird zusammen mit P80 (Motivation) verwendet, wenn die/der Benutzende beabsichtigt, die Zielentität    
**description_en** used with P80 (motivation) for when the user intends to associate a tag with the target entity    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/motivation    
**same as** http://www.w3.org/ns/oa#tagging    
**note_en** Wikibase ID: Q70    
### true    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/true    
**label_de** TRUE    
**label_en** TRUE    
**description_de** Wert für bestimmte Eigenschaften, wie P83 (verifiziert)    
**description_en** value for specific properties, like P83 (verified)    
**type** http://www.w3.org/2002/07/owl#NamedIndividual, https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object    
**same as** https://schema.org/True    
**note_en** Wikibase ID: Q44    
### unknown    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/unknown    
**label_de** unbekannt    
**label_en** unknown    
**description_de** Grad der Sicherheit einer Aussage    
**description_en** degree of certainty of a statement    
**type** http://www.w3.org/2002/07/owl#NamedIndividual    
**subclass of** https://gitlab.com/nfdi4culture/wikibase4research/model/degree_of_certainty    
**note_en** Wikibase ID: Q96    
## **Object Properties**    
### added_by    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/added_by    
**label_de** hinzugefügt durch    
**label_en** added by    
**description_de** verweist auf Teilhinzufügungsereignis    
**description_en** points to part addition event    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P111i_was_added_by    
**note_en** Wikibase ID: P135, Wikibase datatype: wikibase-item    
### affiliation    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/affiliation    
**label_de** Zugehörigkeit    
**label_en** affiliation    
**description_de** Zugehörigkeit einer Person oder Organisation zu einem Gegenstand    
**description_en** affiliation of a person or organisation to an item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P107_has_current_or_former_member, http://www.wikidata.org/entity/P1416, https://schema.org/affiliation    
**note_en** Wikibase ID: P50, Wikibase datatype: wikibase-item    
### annotates    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/annotates    
**label_de** ist Annotation von    
**label_en** annotates    
**description_de** identifiziert die Entität, die das Ziel einer Anmerkung ist    
**description_en** identifies the entity that is the target of an annotation    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/media_item    
**equivalent property** http://www.ics.forth.gr/isl/CRMdig/L43_annotates    
**note_en** Wikibase ID: P77, Wikibase datatype: wikibase-item    
### attribute_assigned_by    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/attribute_assigned_by    
**label_de** Merkmal zugewiesen durch    
**label_en** attribute assigned by    
**description_de** verweist auf Merkmalszuweisungsereignis    
**description_en** points to attribute assignment event    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P140i_was_attributed_by    
**note_en** Wikibase ID: P123, Wikibase datatype: wikibase-item    
### author    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/author    
**label_de** Autor:in    
**label_en** author    
**description_de** Urheber eines Texts    
**description_en** creator of a text    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**note_en** Wikibase ID: P124, Wikibase datatype: wikibase-item    
### by_mother    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/by_mother    
**label_de** durch Mutter    
**label_en** by mother    
**description_de** verknüpft das Ereignis Geburt mit einer Instanz eines Akteurs in der Rolle der gebärenden Mutter    
**description_en** links the event Birth to an instance of an actor in the role of birth-giving mother    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**equivalent property** http://cidoc-crm.org/cidoc-crm/7.1.2/P96_by_mother    
**note_en** Wikibase ID: P40, Wikibase datatype: wikibase-item    
### carried_out_by    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/carried_out_by    
**label_de** wurde ausgeführt von    
**label_en** carried out by    
**description_de** aktiver Akteur eines Ereignisses    
**description_en** active agent of an event    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P14_carried_out_by, https://schema.org/agent    
**note_en** Wikibase ID: P14, Wikibase datatype: wikibase-item    
### classified_as    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/classified_as    
**label_de** klassifiziert als    
**label_en** classified as    
**description_de** ermöglicht die Subtypisierung von Kernentitäten der Ontologie – eine Form der Spezialisierung – durch die Verwendung einer terminologischen Hierarchie oder eines Thesaurus    
**description_en** allows sub-typing of core ontology entities – a form of specialisation – through the use of a terminological hierarchy, or thesaurus    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/type    
**equivalent property** https://cidoc-crm.org/html/cidoc_crm_v7.1.2.html#P2    
**note_en** Wikibase ID: P97, Wikibase datatype: wikibase-item    
### consists_of    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/consists_of    
**label_de** besteht aus    
**label_en** consists of    
**description_de** Material, aus dem ein Objekt hergestellt ist    
**description_en** material an item is made from    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object, https://gitlab.com/nfdi4culture/wikibase4research/model/pysical_object    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/material    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P45_consists_of, http://www.wikidata.org/entity/P186, https://schema.org/material    
**note_en** Wikibase ID: P23, Wikibase datatype: wikibase-item    
### contact_person    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/contact_person    
**label_de** Kontaktperson    
**label_en** contact person    
**description_de** Akteur, welcher die offizielle Anlaufstelle für ein Objekt ist    
**description_en** agent who is the official contact point about an item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object, https://gitlab.com/nfdi4culture/wikibase4research/model/pysical_object    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**note_en** Wikibase ID: P51, Wikibase datatype: wikibase-item    
### created_by    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/created_by    
**label_de** hergestellt durch    
**label_en** created by (event)    
**description_de** verweist auf Herstellungsereignis    
**description_en** points to creation event    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P108i_was_produced_by    
**note_en** Wikibase ID: P132, Wikibase datatype: wikibase-item    
### curator    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/curator    
**label_de** Kurator    
**label_en** curator    
**description_de** Akteur, welcher eine Sammlung kuratiert    
**description_en** agent who curates a collection    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/collection    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P109_has_current_or_former_curator, http://www.wikidata.org/entity/P1640    
**note_en** Wikibase ID: P46, Wikibase datatype: wikibase-item    
### custody_received_by    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/custody_received_by    
**label_de** Gewahrsam übertragen auf    
**label_en** custody received by    
**description_de** neuer Verwahrer dieses Objekts    
**description_en** new custodian of this item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P29_custody_received_by    
**note_en** Wikibase ID: P20, Wikibase datatype: wikibase-item    
### custody_surrendered_by    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/custody_surrendered_by    
**label_de** Gewahrsam übergeben von    
**label_en** custody surrendered by    
**description_de** vorheriger Verwahrer dieses Objekts    
**description_en** previous custodian of this item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/group, https://gitlab.com/nfdi4culture/wikibase4research/model/human    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P28_custody_surrendered_by    
**note_en** Wikibase ID: P19, Wikibase datatype: wikibase-item    
### custody_transferred_by    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/custody_transferred_by    
**label_de** wechselte Besitz durch    
**label_en** custody transferred by    
**description_de** verweist auf Besitztitelwechselereignis    
**description_en** points to change of custody event    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P30i_custody_transferred_through    
**note_en** Wikibase ID: P131, Wikibase datatype: wikibase-item    
### depicts    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/depicts    
**label_de** bildet ab    
**label_en** depicts    
**description_de** Konzept, das auf einem Objekt abgebildet ist    
**description_en** concept that is depicted on an item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object, https://gitlab.com/nfdi4culture/wikibase4research/model/pysical_object    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P62_depicts, http://www.wikidata.org/entity/P180    
**note_en** Wikibase ID: P64, Wikibase datatype: wikibase-item    
### destroyed_by    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/destroyed_by    
**label_de** zerstört durch    
**label_en** destroyed by    
**description_de** verweist auf Zerstörungsereignis    
**description_en** points to destruction event    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P13i_was_destroyed_by    
**note_en** Wikibase ID: P120, Wikibase datatype: wikibase-item    
### died    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/died    
**label_de** Tod    
**label_en** death    
**description_de** verweist auf Todesereignis    
**description_en** points to death event    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P100i_died_in    
**note_en** Wikibase ID: P119, Wikibase datatype: wikibase-item    
### documented_in    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/documented_in    
**label_de** wird belegt in    
**label_en** documented in    
**description_de** verweist auf einen bibliografischen Titel, der diesen Titel dokumentiert oder weitere Informationen über ihn liefert    
**description_en** points to a bibliographic item which documents this item or provides further information about it    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object, https://gitlab.com/nfdi4culture/wikibase4research/model/pysical_object    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/bibliographic_work    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P70_documents    
**note_en** Wikibase ID: P58, Wikibase datatype: wikibase-item    
### from_father    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/from_father    
**label_de** gab Vaterschaft    
**label_en** from father    
**description_de** verknüpft das Ereignis Geburt mit einer Instanz eines Akteurs in der Rolle des biologischen Vaters    
**description_en** links the event Birth to an instance of an actor in the role of biological father    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**equivalent property** http://cidoc-crm.org/cidoc-crm/7.1.2/P97_from_father    
**note_en** Wikibase ID: P41, Wikibase datatype: wikibase-item    
### has_annotation    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/has_annotation    
**label_de** hat Annotation    
**label_en** annotation    
**description_de** Anmerkung, die für dieses Medienelement gemacht wurde    
**description_en** annotation that was done for this media item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/media_item    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**equivalent property** http://www.ics.forth.gr/isl/CRMdig/L43_annotates    
**note_en** Wikibase ID: P75, Wikibase datatype: wikibase-item    
### has_condition    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/has_condition    
**label_de** hat Zustand    
**label_en** condition    
**description_de** Zustand eines Gegenstands    
**description_en** condition of an object    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object, https://gitlab.com/nfdi4culture/wikibase4research/model/pysical_object    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/condition    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P44_has_condition    
**note_en** Wikibase ID: P26, Wikibase datatype: wikibase-item    
### has_degree_of_certainty    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/has_degree_of_certainty    
**label_de** Grad der Sicherheit    
**label_en** degree of certainty    
**description_de** Grad der Sicherheit einer Aussage; kann niedrig, mittel, hoch oder unbekannt sein    
**description_en** degree of certainty for a statement, can be low, mid, high or unknown    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**note_en** Wikibase ID: P122, Wikibase datatype: wikibase-item    
### has_event    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/has_event    
**label_de** hat Ereignis    
**label_en** event    
**description_de** etwas, das mit diesem Objekt passiert ist    
**description_en** something that happened to this item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/human-made_object    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**note_en** Wikibase ID: P8, Wikibase datatype: wikibase-item    
### has_file_format    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/has_file_format    
**label_de** hat Datenformat    
**label_en** file format    
**description_de** Format der Datei    
**description_en** format of the file    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/media_item    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/file_format    
**equivalent property** http://www.wikidata.org/entity/P2701, https://schema.org/encodingFormat    
**note_en** Wikibase ID: P70, Wikibase datatype: wikibase-item    
### has_function    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/has_function    
**label_de** Funktion    
**label_en** function    
**description_de** Zweck oder Verwendung eines Objekts    
**description_en** purpose or use of an item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/function    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P101_had_as_general_use, http://www.wikidata.org/entity/P366    
**note_en** Wikibase ID: P137, Wikibase datatype: wikibase-item    
### has_mime_type    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/has_mime_type    
**label_de** MIME Typ    
**label_en** MIME type    
**description_de** Standard der das Format einer Datei angibt    
**description_en** standard indicating the format of a file    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/media_item    
**note_en** Wikibase ID: P112, Wikibase datatype: wikibase-item    
### has_motivation    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/has_motivation    
**label_de** hat Motivation    
**label_en** motivation    
**description_de** eine Eigenschaft aus dem W3C-Anmerkungsstandard, die die Gründe für die Erstellung einer Anmerkung angibt    
**description_en** a property from the W3C annotation standard providing the reasons why an annotation was made    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/motivation    
**equivalent property** http://www.w3.org/ns/oa#motivatedBy    
**note_en** Wikibase ID: P80, Wikibase datatype: wikibase-item    
### has_occupation    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/has_occupation    
**label_de** Beruf    
**label_en** occupation    
**description_de** Beruf einer Person    
**description_en** occuption or profession of a person    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/human    
**equivalent property** http://www.wikidata.org/entity/P106    
**note_en** Wikibase ID: P121, Wikibase datatype: wikibase-item    
### has_parent    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/has_parent    
**label_de** hat Elternteil    
**label_en** has parent    
**description_de** familiäre Beziehung    
**description_en** familial relationship    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**note_en** Wikibase ID: P118, Wikibase datatype: wikibase-item    
### has_part    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/has_part    
**label_de** hat Teil    
**label_en** has part    
**description_de** ein anderes Objekt, das Teil dieses Objekts ist    
**description_en** another item that is part of this item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P45_consists_of, http://www.wikidata.org/entity/P527, https://schema.org/hasPart    
**note_en** Wikibase ID: P5, Wikibase datatype: wikibase-item    
### has_position    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/has_position    
**label_de** hat Position    
**label_en** position    
**description_de** gibt die Position eines Objekts innerhalb eines Standorts an    
**description_en** indicates the position of an item within a location    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object, https://gitlab.com/nfdi4culture/wikibase4research/model/pysical_object    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/position    
**note_en** Wikibase ID: P39, Wikibase datatype: wikibase-item    
### has_sex_or_gender    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/has_sex_or_gender    
**label_de** hat Geschlecht    
**label_en** sex or gender    
**description_de** Geschlecht oder Geschlechtsidentität einer Person    
**description_en** sex or gender identity of a person    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/human    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/sex_or_gender    
**equivalent property** http://www.wikidata.org/entity/P21    
**note_en** Wikibase ID: P49, Wikibase datatype: wikibase-item    
### in_custody_of    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/in_custody_of    
**label_de** in Gewahrsam von    
**label_en** in custody of    
**description_de** Agent, welcher eine Objekt verwahrt    
**description_en** agent who holds an item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/human-made_object    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P49_has_former_or_current_keeper    
**note_en** Wikibase ID: P43, Wikibase datatype: wikibase-item    
### instance_of    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/instance_of    
**label_de** ist ein(e)    
**label_en** instance of    
**description_de** dieses Objekt ist ein spezifisches Beispiel und gehört zu dieser Klasse    
**description_en** this item is a specific example and a member of that class    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**equivalent property** http://www.wikidata.org/entity/P31    
**note_en** Wikibase ID: P1, Wikibase datatype: wikibase-item    
### language_of_work_or_name    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/language_of_work_or_name    
**label_de** Sprache des Werks oder des Namens    
**label_en** language of work or name    
**description_de** Sprache dieses Werkes oder Namens    
**description_en** language associated with this creative work or a name    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**note_en** Wikibase ID: P110, Wikibase datatype: wikibase-item    
### license    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/license    
**label_de** Lizenz    
**label_en** license    
**description_de** die Lizenz, die die Nutzungsrechte für diesen Artikel klärt (verwenden Sie gegebenenfalls auch die Eigenschaft »zitieren als«, um die richtige Zitierung anzugeben)    
**description_en** the license that clarifies use rights for this item (also use property 'cite as' to indicate the proper citation if applicable)    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/license    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P104_is_subject_to, http://www.wikidata.org/entity/P275, https://schema.org/license    
**note_en** Wikibase ID: P53, Wikibase datatype: wikibase-item    
### located_in_country    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/located_in_country    
**label_de** Land    
**label_en** country    
**description_de** gibt an, in welchem Land sich eine Entität befindet    
**description_en** states which country an entity is located in    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/country    
**equivalent property** http://www.wikidata.org/entity/P17    
**note_en** Wikibase ID: P127, Wikibase datatype: wikibase-item    
### location    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/location    
**label_de** Standort    
**label_en** location    
**description_de** beschreibt, wo sich ein Objekt befindet    
**description_en** describes where an item is located    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/place    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P53_has_former_or_current_location, http://www.wikidata.org/entity/P276, https://schema.org/location    
**note_en** Wikibase ID: P38, Wikibase datatype: wikibase-item    
### material_used    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/material_used    
**label_de** verwendetes Material    
**label_en** material used    
**description_de** Material, das zur Erstellung oder Modifikation eines Objekts verwendet wird    
**description_en** material used for creating or changing an item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/material    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P126_employed    
**note_en** Wikibase ID: P22, Wikibase datatype: wikibase-item    
### method    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/method    
**label_de** hat Verfahren    
**label_en** method    
**description_de** Technik oder Methode, die zur Erstellung oder Änderung eines Gegenstands verwendet wird    
**description_en** technique or method that is used for creating or changing an object    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/media_item    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/technique    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P32_used_general_technique    
**note_en** Wikibase ID: P65, Wikibase datatype: wikibase-item    
### modified_by    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/modified_by    
**label_de** wurde verändert durch    
**label_en** modified by    
**description_de** verweist auf Modifikationsereignis    
**description_en** points to modifcation event    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P31i_was_modified_by    
**note_en** Wikibase ID: P133, Wikibase datatype: wikibase-item    
### moved_by    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/moved_by    
**label_de** Ortswechsel durch    
**label_en** moved by    
**description_de** Verweist auf Ortswechselereignis    
**description_en** points to move event    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P25i_moved_by    
**note_en** Wikibase ID: P134, Wikibase datatype: wikibase-item    
### moved_from    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/moved_from    
**label_de** Ortswechsel von    
**label_en** moved from    
**description_de** früherer Standort dieses Objekts    
**description_en** previous location of this item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/place    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P27_moved_from    
**note_en** Wikibase ID: P18, Wikibase datatype: wikibase-item    
### moved_to    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/moved_to    
**label_de** Ortswechsel nach    
**label_en** moved to    
**description_de** neuer Standort dieses Objekts    
**description_en** new location of this item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/place    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P26_moved_to    
**note_en** Wikibase ID: P17, Wikibase datatype: wikibase-item    
### object_of_representation    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/object_of_representation    
**label_de** Gegenstand der Darstellung    
**label_en** object of representation    
**description_de** das Objekt, das durch dieses Medienelement dargestellt wird    
**description_en** the item that is represented by this media item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/media_item    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/pysical_object    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P138_represents    
**note_en** Wikibase ID: P63, Wikibase datatype: wikibase-item    
### owner    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/owner    
**label_de** Eigentümer    
**label_en** owner    
**description_de** Agent, welcher ein Objekt besitzt    
**description_en** agent who owns an item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/human-made_object    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P51_has_former_or_current_owner, http://www.wikidata.org/entity/P127    
**note_en** Wikibase ID: P44, Wikibase datatype: wikibase-item    
### ownership_changed_by    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/ownership_changed_by    
**label_de** Eigentümerwechsel durch    
**label_en** ownership changed by    
**description_de** verweist auf Eigentumswechselereignis    
**description_en** points to change of ownership event    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P24i_changed_ownership_through    
**note_en** Wikibase ID: P117, Wikibase datatype: wikibase-item    
### parent_of    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/parent_of    
**label_de** ist Elternteil von    
**label_en** parent of    
**description_de** assoziiert eine Instanz von Mensch mit einer anderen Instanz von Mensch, die die Rolle des Kindes der ersten Instanz spielt    
**description_en** associates an instance of Human with another instance of Human who plays the role of the first instances child    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/human    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/human    
**equivalent property** http://cidoc-crm.org/cidoc-crm/7.1.2/P152_has_parent    
**note_en** Wikibase ID: P48, Wikibase datatype: wikibase-item    
### part_added    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/part_added    
**label_de** Teil hinzugefügt    
**label_en** part added    
**description_de** welcher Teil zu diesem Objekt hinzugefügt wurde    
**description_en** which part was added to this item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/human-made_object    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P111_added    
**note_en** Wikibase ID: P28, Wikibase datatype: wikibase-item    
### part_of    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/part_of    
**label_de** ist Teil von    
**label_en** part of    
**description_de** das Objekt, zu dem dieses Objekt gehört    
**description_en** the item that this item is a part of    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P46_is_composed_of, http://www.wikidata.org/entity/P361, https://schema.org/isPartOf    
**note_en** Wikibase ID: P6, Wikibase datatype: wikibase-item    
### part_removed    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/part_removed    
**label_de** Teil entfernt    
**label_en** part removed    
**description_de** welcher Teil von diesem Objekt entfernt wurde    
**description_en** which part was removed from this item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/human-made_object    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P113_removed    
**note_en** Wikibase ID: P27, Wikibase datatype: wikibase-item    
### participant    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/participant    
**label_de** hatte Teilnehmer    
**label_en** participant    
**description_de** Person, die an einem Ereignis teilgenommen hat    
**description_en** person who participated in an event    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P11_had_participant, http://www.wikidata.org/entity/P710, https://schema.org/participant    
**note_en** Wikibase ID: P13, Wikibase datatype: wikibase-item    
### placeholder    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/placeholder    
**label_de** Platzhalter    
**label_en** placeholder    
**description_de** Platzhalterobjekt    
**description_en** placeholder property    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**note_en** Wikibase ID: P21, Wikibase datatype: wikibase-item    
### publisher    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/publisher    
**label_de** Verlag    
**label_en** publisher    
**description_de** Herausgeber von Werken    
**description_en** entity that publishes works    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**note_en** Wikibase ID: P125, Wikibase datatype: wikibase-item    
### raw_data_created_by    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/raw_data_created_by    
**label_de** Rohdaten hergestellt durch    
**label_en** raw data created by (event)    
**description_de** verweist auf Herstellungsereignis der Rohdaten    
**description_en** points to raw data creation event    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**note_en** Wikibase ID: P111, Wikibase datatype: wikibase-item    
### related_concept    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/related_concept    
**label_de** verwandter Begriff    
**label_en** related concept    
**description_de** verwenden Sie diese Eigenschaft, um den Anmerkungen Elementbeziehungen hinzuzufügen    
**description_en** use this property to add item relations to annotations    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object    
**note_en** Wikibase ID: P81, Wikibase datatype: wikibase-item    
### related_media    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/related_media    
**label_de** zugehörige Medien    
**label_en** related media    
**description_de** verwenden Sie diese Eigenschaft, um Medienbeziehungen zu Anmerkungen hinzuzufügen    
**description_en** use this property to add media relations to annotations    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/media_item    
**note_en** Wikibase ID: P82, Wikibase datatype: wikibase-item    
### removed_by    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/removed_by    
**label_de** entfernt durch    
**label_en** removed by    
**description_de** verweist auf Teilentfernungsereignis    
**description_en** points to part removal event    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P113i_was_removed_by    
**note_en** Wikibase ID: P136, Wikibase datatype: wikibase-item    
### representation    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/representation    
**label_de** hat Darstellung    
**label_en** representation    
**description_de** Medienelement, das dieses Objekt darstellt    
**description_en** media item that represents this item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/pysical_object    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/media_item    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P138_represents    
**note_en** Wikibase ID: P62, Wikibase datatype: wikibase-item    
### resulted_in    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/resulted_in    
**label_de** ergab    
**label_en** resulted in    
**description_de** neues Objekt, das durch eine Transformation entstanden ist    
**description_en** new item created by a transformation    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/human-made_object    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P123_resulted_in    
**note_en** Wikibase ID: P29, Wikibase datatype: wikibase-item    
### right_held_by    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/right_held_by    
**label_de** Rechte gehalten von    
**label_en** right held by    
**description_de** identifiziert den Akteur, der die Rechte an einem Objekt besitzt    
**description_en** identifies the agent who owns the rights to an item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/media_item    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**equivalent property** http://cidoc-crm.org/cidoc-crm/7.1.2/P105_right_held_by    
**note_en** Wikibase ID: P45, Wikibase datatype: wikibase-item    
### sibling_of    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/sibling_of    
**label_de** ist Geschwisterteil von    
**label_en** sibling of    
**description_de** assoziiert eine Instanz von Mensch mit einer anderen Instanz von Mensch, die die Rolle des Geschwisterteils der ersten Instanz spielt    
**description_en** associates an instance of Human with another instance of Human who plays the role of the first instances sibling    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/human    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/human    
**note_en** Wikibase ID: P47, Wikibase datatype: wikibase-item    
### software_used    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/software_used    
**label_de** hat Software    
**label_en** software    
**description_de** die für die Erstellung des Medienelements verwendete Software    
**description_en** software used for creation of media item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/media_item    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/software    
**note_en** Wikibase ID: P66, Wikibase datatype: wikibase-item    
### spouse    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/spouse    
**label_de** Ehepartner    
**label_en** spouse    
**description_de** das Subjekt hat das Objekt als seinen/ihren Ehepartner (Ehemann, Ehefrau, Partner usw.)    
**description_en** the subject has the object as their spouse (husband, wife, partner, etc.)    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**equivalent property** http://www.wikidata.org/entity/P26    
**note_en** Wikibase ID: P42, Wikibase datatype: wikibase-item    
### stated_in    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/stated_in    
**label_de** angegeben in    
**label_en** stated in    
**description_de** verweist auf den bibliografischen Eintrag, in dem eine Behauptung angegeben wurde – zu verwenden im Feld Referenzen unter einer Behauptung    
**description_en** points to the bibliographic item where a claim was stated in - to be used in the references field under a statement    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/bibliographic_work    
**equivalent property** http://www.wikidata.org/entity/P248    
**note_en** Wikibase ID: P55, Wikibase datatype: wikibase-item    
### style_used    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/style_used    
**label_de** Stil    
**label_en** style used    
**description_de** Stil eines Kulturguts    
**description_en** style that was used in the creation or modification of an item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**note_en** Wikibase ID: P107, Wikibase datatype: wikibase-item    
### subclass_of    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/subclass_of    
**label_de** Unterklasse von    
**label_en** subclass of    
**description_de** verweist auf die Oberklasse dieser Klasse    
**description_en** points to the superclass of this class    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**equivalent property** http://www.wikidata.org/entity/P279    
**note_en** Wikibase ID: P2, Wikibase datatype: wikibase-item    
### subproperty_of    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/subproperty_of    
**label_de** Untereigenschaft von    
**label_en** subproperty of    
**description_de** verweist auf die übergeordnete Eigenschaft dieser Eigenschaft    
**description_en** points to the superproperty of this property    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**equivalent property** http://www.wikidata.org/entity/P1647    
**note_en** Wikibase ID: P3, Wikibase datatype: wikibase-property    
### took_place_at    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/took_place_at    
**label_de** fand statt in    
**label_en** took place at    
**description_de** Ort eines Ereignisses    
**description_en** location of an event    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/place    
**note_en** Wikibase ID: P9, Wikibase datatype: wikibase-item    
### transferred_title_from    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/transferred_title_from    
**label_de** Eigentum übertragen von    
**label_en** transferred title from    
**description_de** bei Eigentümerwechsel: neuer Eigentümer    
**description_en** for ownership changes: new owner    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P23_transferred_title_from    
**note_en** Wikibase ID: P16, Wikibase datatype: wikibase-item    
### transferred_title_to    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/transferred_title_to    
**label_de** Eigentum übertragen auf    
**label_en** transferred title to    
**description_de** bei Besitztitelwechsel: vorheriger Besitzer    
**description_en** for ownership changes: previous owner    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/actor    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P22_transferred_title_to    
**note_en** Wikibase ID: P15, Wikibase datatype: wikibase-item    
### transformed_by    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/transformed_by    
**label_de** wurde umgewandelt durch    
**label_en** transformed by    
**description_de** verweist auf ein Umwandlungsereignis    
**description_en** points to transformation event    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P124i_was_transformed_by    
**note_en** Wikibase ID: P128, Wikibase datatype: wikibase-item    
### used_for    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/used_for    
**label_de** benutzt für    
**label_en** used for    
**description_de** Zweck oder Verwendung eines Objekts    
**description_en** purpose or use of an item    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** https://gitlab.com/nfdi4culture/wikibase4research/model/function    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P101_had_as_general_use, http://www.wikidata.org/entity/P366    
**note_en** Wikibase ID: P30, Wikibase datatype: wikibase-item    
### verified    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/verified    
**label_de** verifiziert    
**label_en** verified    
**description_de** Status einer Anmerkung vor oder nach der Überprüfung durch einen Benutzer mit höheren Bearbeitungsrechten (normalerweise true oder false)    
**description_en** the status of an annotation before or after review by a user with higher editing privileges (usually true or false)    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** http://www.w3.org/2001/XMLSchema#boolean    
**note_en** Wikibase ID: P83, Wikibase datatype: wikibase-item    
### was_born    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/was_born    
**label_de** Geburt    
**label_en** birth    
**description_de** verweist auf Geburtsereignis    
**description_en** points to birth event    
**type** http://www.w3.org/2002/07/owl#ObjectProperty    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P98i_was_born    
**note_en** Wikibase ID: P115, Wikibase datatype: wikibase-item    
## **Datatype Properties**    
### address    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/address    
**label_de** Adresse    
**label_en** address    
**description_de** Adresse eines Objektes, in der Regel eines Gebäudes oder einer Organisation    
**description_en** street address of an item, usually a building or organisation    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** http://www.w3.org/2001/XMLSchema#string    
**equivalent property** http://www.wikidata.org/entity/P6375, https://schema.org/address    
**note_en** Wikibase ID: P36, Wikibase datatype: string    
### alive_during    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/alive_during    
**label_de** lebt zur Zeit    
**label_en** alive during    
**description_de** Zeitpunkt oder Zeitrahmen, in dem eine Person am Leben ist oder war    
**description_en** point in time or interval when someone is or was alive    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/human    
**range** http://www.w3.org/2001/XMLSchema#date    
**note_en** Wikibase ID: P108, Wikibase datatype: edtf    
### annotation_text    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation_text    
**label_de** Anmerkungstext    
**label_en** annotation text    
**description_de** Link zur URL, die den vollständigen Text enthält    
**description_en** link to the URL that has the full text    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** http://www.w3.org/2001/XMLSchema#string    
**note_en** Wikibase ID: P76, Wikibase datatype: url    
### bamberg_vocab_id    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/bamberg_vocab_id    
**label_de** Bamberg Vocab ID    
**label_en** Bamberg Vocab ID    
**description_de** Identifikator aus dem Bamberger Vokabular für historische Architektur    
**description_en** identifier from Bamberg's Vocabulary for Historical Architecture    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**note_en** Wikibase ID: P114, Wikibase datatype: external-id    
### bears_feature    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/bears_feature    
**label_de** trägt Merkmal    
**label_en** bears feature    
**description_de** Merkmal eines Gegenstand    
**description_en** feature of an object    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** http://www.w3.org/2001/XMLSchema#string    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P56_bears_feature    
**note_en** Wikibase ID: P24, Wikibase datatype: string    
### camera_type    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/camera_type    
**label_de** Kameratyp    
**label_en** camera type    
**description_de** Kompakkt-spezifische Eigenschaft, die sich auf die Perspektive der Kamera bei der Beschriftung eines 3D-Modells bezieht    
**description_en** Kompakkt-specific property relating to the perspective of the camera when annotating a 3D model    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** http://www.w3.org/2001/XMLSchema#string    
**note_en** Wikibase ID: P78, Wikibase datatype: string    
### conforms_to    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/conforms_to    
**label_de** stimmt überein mit    
**label_en** conforms to    
**description_de** Norm, welcher die Datei entspricht    
**description_en** which standard the file conforms to    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/digital_object    
**range** http://www.w3.org/2001/XMLSchema#string    
**note_en** Wikibase ID: P72, Wikibase datatype: string    
### contact_point    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/contact_point    
**label_de** Kontaktpunkt    
**label_en** contact point    
**description_de** wie eine Organisation oder Gruppe kontaktiert werden kann    
**description_en** how an organisation or group can be contacted    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/group    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P76_has_contact_point    
**note_en** Wikibase ID: P129, Wikibase datatype: string    
### coordinate_location    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/coordinate_location    
**label_de** geographische Koordinaten    
**label_en** coordinate location    
**description_de** genauer Standort eines Objekts    
**description_en** exact location of an item    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object, https://gitlab.com/nfdi4culture/wikibase4research/model/place    
**range** http://www.w3.org/2001/XMLSchema#string    
**equivalent property** http://www.wikidata.org/entity/P625, https://schema.org/geo    
**note_en** Wikibase ID: P37, Wikibase datatype: globe-coordinate    
### copyright_statement    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/copyright_statement    
**label_de** Urheberrechtserklärung    
**label_en** copyright statement    
**description_de** wie Sie den Artikel in Übereinstimmung mit der Lizenz zitieren (verwenden Sie die Eigenschaft „Lizenz“, um die Nutzungsrechte anzugeben)    
**description_en** how to cite this item in compliance with the license (also use property 'license' to indicate usage rights)    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object, https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** http://www.w3.org/2001/XMLSchema#string    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P105_right_held_by    
**note_en** Wikibase ID: P130, Wikibase datatype: string    
### date    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/date    
**label_de** Datum    
**label_en** date    
**description_de** wird für Ereignisse verwendet, die mit einem Zeitpunkt und nicht mit einer Zeitspanne verbunden sind (verwenden Sie Start- und Enddatum zur Angabe einer Zeitspanne)    
**description_en** used for events that are associated with a point in time instead of a time span (use start date and end date for indicating a time span)    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** http://www.w3.org/2001/XMLSchema#date    
**equivalent property** http://www.wikidata.org/entity/P585    
**note_en** Wikibase ID: P12, Wikibase datatype: edtf    
### diameter    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/diameter    
**label_de** Durchmesser    
**label_en** diameter    
**description_de** Durchmesser eines Objekts    
**description_en** diameter of an item    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**subproperty of** https://gitlab.com/nfdi4culture/wikibase4research/model/has_dimension    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** http://www.w3.org/2001/XMLSchema#float    
**equivalent property** https://www.wikidata.org/entity/P2386    
**note_en** Wikibase ID: P105, Wikibase datatype: quantity    
### dimension    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/dimension    
**label_de** hat Dimension    
**label_en** dimension    
**description_de** übergeordnete Eigenschaft für Abmessungen wie Höhe und Breite    
**description_en** superproperty for dimensions like height and width    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object, https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P43_has_dimension    
**note_en** Wikibase ID: P31, Wikibase datatype: quantity    
### doi    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/doi    
**label_de** DOI    
**label_en** DOI    
**description_de** Seriencode zur eindeutigen Identifizierung digitaler Objekte wie wissenschaftlicher Arbeiten (nur Großbuchstaben verwenden)    
**description_en** serial code used to uniquely identify digital objects like academic papers (use upper case letters only)    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/digital_object    
**range** http://www.w3.org/2001/XMLSchema#string    
**equivalent property** http://www.wikidata.org/entity/P356    
**note_en** Wikibase ID: P103, Wikibase datatype: external-id    
### duration    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/duration    
**label_de** Dauer    
**label_en** duration    
**description_de** Dauer eines Objekts, in der Regel Video oder Audio    
**description_en** duration of an item, usually video or audio    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**subproperty of** https://gitlab.com/nfdi4culture/wikibase4research/model/has_dimension    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object, https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** http://www.w3.org/2001/XMLSchema#string    
**equivalent property** http://www.wikidata.org/entity/P2047, https://schema.org/duration    
**note_en** Wikibase ID: P68, Wikibase datatype: quantity    
### end_date    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/end_date    
**label_de** Enddatum    
**label_en** end date    
**description_de** wenn ein Ereignis beendet wurde, auch die Eigenschaft »Startdatum« verwenden (die Eigenschaft »Datum« sollte alternativ verwendet werden, wenn ein Ereignis nur einen Zeitpunkt statt einer Zeitspanne hat)    
**description_en** when an event finished, use property 'start date' as well (the property 'date' should be used alternatively when an event only has a point in time instead of a time span)    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** http://www.w3.org/2001/XMLSchema#date    
**equivalent property** http://www.wikidata.org/entity/P582, https://schema.org/endDate    
**note_en** Wikibase ID: P11, Wikibase datatype: edtf    
### equipment    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/equipment    
**label_de** Ausrüstung    
**label_en** equipment    
**description_de** für die Erstellung von Medienobjekten verwendete Ausrüstung    
**description_en** equipment used for creation of media item    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/media_item    
**range** http://www.w3.org/2001/XMLSchema#string    
**note_en** Wikibase ID: P67, Wikibase datatype: string    
### event_description    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/event_description    
**label_de** Beschreibung des Ereignisses    
**label_en** event description    
**description_de** Freitextfeld zur Beschreibung von Ereignissen    
**description_en** free text description field for events    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** http://www.w3.org/2001/XMLSchema#string    
**note_en** Wikibase ID: P106, Wikibase datatype: string    
### external_image    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/external_image    
**label_de** externer Link zu Bild    
**label_en** external image URL    
**description_de** URL zu visueller Repräsentation des Objekts    
**description_en** URL that points to a visual representation of this item    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/human_made_object    
**range** http://www.w3.org/2001/XMLSchema#string    
**note_en** Wikibase ID: P116, Wikibase datatype: url    
### external_link    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/external_link    
**label_de** externer Link    
**label_en** external link    
**description_de** verweist auf externe Ressourcen oder Mediendarstellungen    
**description_en** links to external resources or media representations    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/media_item    
**range** http://www.w3.org/2001/XMLSchema#string    
**note_en** Wikibase ID: P57, Wikibase datatype: url    
### factgrid_id    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/factgrid_id    
**label_de** Factgrid ID    
**label_en** Factgrid id    
**description_de** Identifikator aus Factgrid    
**description_en** identifier from Factgrid    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**note_en** Wikibase ID: P109, Wikibase datatype: external-id    
### file_extension    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/file_extension    
**label_de** Dateierweiterung    
**label_en** file extension    
**description_de** Dateierweiterung, die das Dateiformat angibt, das mit dem Klassen-Dateiformat verwendet wird    
**description_en** file extension that denotes the file format use with class file format    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/file_format    
**range** http://www.w3.org/2001/XMLSchema#string    
**equivalent property** http://www.wikidata.org/entity/P1195    
**note_en** Wikibase ID: P71, Wikibase datatype: string    
### file_size    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/file_size    
**label_de** Dateigröße    
**label_en** file size    
**description_de** Größe einer Medienelement-Datei    
**description_en** size of media item file    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/media_item    
**equivalent property** http://www.wikidata.org/entity/P3575    
**note_en** Wikibase ID: P69, Wikibase datatype: quantity    
### file_storage    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/file_storage    
**label_de** Dateispeicher    
**label_en** file storage    
**description_de** URL, unter der die Datei gespeichert ist    
**description_en** URL where file is stored    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/media_item    
**range** http://www.w3.org/2001/XMLSchema#string    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P43_has_dimension    
**note_en** Wikibase ID: P73, Wikibase datatype: url    
### file_view    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/file_view    
**label_de** Dateiansicht    
**label_en** file view    
**description_de** URL, unter der die Datei eingesehen werden kann    
**description_en** URL where file can be viewed    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/media_item    
**range** http://www.w3.org/2001/XMLSchema#string    
**note_en** Wikibase ID: P74, Wikibase datatype: url    
### formatter_uri    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/formatter_uri    
**label_de** URI-Formatierer für RDF-Ressource    
**label_en** formatter uri for rdf resource    
**description_de** URI-ähnliche Zeichenkette, wie "https://wikidata.org/wiki/$1/", bei der "$1" automatisch ersetzt wird mit dem tatsächlichen Eigenschaftswert eines Datenobjekts (URI der Ressource, nicht der RDF-Datei)    
**description_en** URI template from which "$1" can be automatically replaced with the effective property value on items (it is the URI of the resources, not the URI of the RDF file describing it)    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**note_en** Wikibase ID: P54, Wikibase datatype: string    
### formatter_url    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/formatter_url    
**label_de** URL-Formatierer    
**label_en** formatter url    
**description_de** URL-ähnliche Zeichenkette, wie "https://wikidata.org/wiki/$1/", bei der "$1" automatisch ersetzt wird mit dem tatsächlichen Eigenschaftswert eines Datenobjekts (genutzt bei der Definition von Eigenschaften)    
**description_en** web page URL; URI template from which "$1" can be automatically replaced with the effective property value on items. If the site goes offline, set it to deprecated rank. If the formatter URL changes, add a new statement with preferred rank.    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**note_en** Wikibase ID: P52, Wikibase datatype: string    
### full_citation    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/full_citation    
**label_de** vollständige Quellenangabe    
**label_en** full citation    
**description_de** wie ein bibliographischer Titel zitiert werden soll    
**description_en** how a bibliographic item a would be cited    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/bibliographic_work    
**range** http://www.w3.org/2001/XMLSchema#string    
**note_en** Wikibase ID: P59, Wikibase datatype: string    
### geonames    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/geonames    
**label_de** Geonames    
**label_en** Geonames    
**description_de** Kennung in der GeoNames geographical database    
**description_en** identifier in the GeoNames geographical database    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/place    
**range** http://www.w3.org/2001/XMLSchema#string    
**equivalent property** http://www.wikidata.org/entity/P1566    
**note_en** Wikibase ID: P101, Wikibase datatype: external-id    
### getty_aat    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/getty_aat    
**label_de** Getty AAT    
**label_en** Getty AAT    
**description_de** Kennung im Art & Architecture Thesaurus des Getty Research Institute    
**description_en** identifier in the Art & Architecture Thesaurus by the Getty Research Institute    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/human-made_object    
**range** http://www.w3.org/2001/XMLSchema#string    
**equivalent property** http://www.wikidata.org/entity/P1014    
**note_en** Wikibase ID: P99, Wikibase datatype: external-id    
### getty_ulan    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/getty_ulan    
**label_de** Getty ULAN    
**label_en** Getty ULAN    
**description_de** Kennung aus der Union List of Artist Names des Getty Research Institute    
**description_en** identifier from the Union List of Artist Names by the Getty Research Institute    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/human    
**range** http://www.w3.org/2001/XMLSchema#string    
**equivalent property** http://www.wikidata.org/entity/P245    
**note_en** Wikibase ID: P100, Wikibase datatype: external-id    
### gnd    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/gnd    
**label_de** GND    
**label_en** GND    
**description_de** Kennung aus einer internationalen Normdatei für Personennamen, Körperschaften und Schlagwörter – Deutsche Nationalbibliothek    
**description_en** identifier from an international authority file of names, subjects, and organizations - Deutsche Nationalbibliothek    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/actor, https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** http://www.w3.org/2001/XMLSchema#string    
**equivalent property** http://www.wikidata.org/entity/P227    
**note_en** Wikibase ID: P102, Wikibase datatype: external-id    
### height    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/height    
**label_de** Höhe    
**label_en** height    
**description_de** Höhe eines Objekts    
**description_en** height of an item    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**subproperty of** https://gitlab.com/nfdi4culture/wikibase4research/model/has_dimension    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** http://www.w3.org/2001/XMLSchema#float    
**equivalent property** http://www.wikidata.org/entity/P2048, https://schema.org/height    
**note_en** Wikibase ID: P32, Wikibase datatype: quantity    
### iconclass    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/iconclass    
**label_de** Iconclass    
**label_en** Iconclass    
**description_de** Iconclass-Code, der einem künstlerischen Motiv oder Konzept entspricht    
**description_en** Iconclass code that corresponds with an artistic theme or concept    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/iconographic_concept    
**range** http://www.w3.org/2001/XMLSchema#string    
**equivalent property** http://www.wikidata.org/entity/P1256    
**note_en** Wikibase ID: P98, Wikibase datatype: external-id    
### image    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/image    
**label_de** Bild    
**label_en** image    
**description_de** visuelle Darstellung dieses Objekts, die in der Regel nur zur Dokumentation und nicht zur Darstellung verwendet wird (siehe auch P32)    
**description_en** visual depiction of this item, typically used for documentation only rather than representation (see also P32)    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation, https://gitlab.com/nfdi4culture/wikibase4research/model/medial_item    
**range** http://www.w3.org/2001/XMLSchema#string    
**equivalent property** http://www.wikidata.org/entity/P18, https://schema.org/image    
**note_en** Wikibase ID: P61, Wikibase datatype: localMedia    
### inscription    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/inscription    
**label_de** Inschrift    
**label_en** inscription    
**description_de** Textstück auf einem Gegenstand    
**description_en** piece of text on an object    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** http://www.w3.org/2001/XMLSchema#string    
**equivalent property** http://www.wikidata.org/entity/P1684    
**note_en** Wikibase ID: P25, Wikibase datatype: string    
### internal_id    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/internal_id    
**label_de** interne ID    
**label_en** internal ID    
**description_de** interne Kennung für diesen Artikel    
**description_en** Internal identifier for this item    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** http://www.w3.org/2001/XMLSchema#string    
**note_en** Wikibase ID: P96, Wikibase datatype: string    
### issn    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/issn    
**label_de** issn    
**label_en** issn    
**description_de** Identifikator für Zeitschriften    
**description_en** identifier for journals    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**note_en** Wikibase ID: P126, Wikibase datatype: external-id    
### length    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/length    
**label_de** Länge    
**label_en** length    
**description_de** Länge eines Objekts    
**description_en** length of an item    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**subproperty of** https://gitlab.com/nfdi4culture/wikibase4research/model/has_dimension    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** http://www.w3.org/2001/XMLSchema#float    
**equivalent property** http://www.wikidata.org/entity/P2043    
**note_en** Wikibase ID: P33, Wikibase datatype: quantity    
### number_of_parts    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/number_of_parts    
**label_de** hat Anzahl Teile    
**label_en** number of parts    
**description_de** bei Objekten, die aus Teilen bestehen: wie viele Teile es gibt    
**description_en** for items that have parts: how many parts there are    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/human-made_object    
**range** http://www.w3.org/2001/XMLSchema#float    
**equivalent property** http://www.cidoc-crm.org/cidoc-crm/P57_has_number_of_parts    
**note_en** Wikibase ID: P7, Wikibase datatype: quantity    
### position_in_3d_model_-_perspective_position_x-axis    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/position_in_3d_model_-_perspective_position_x-axis    
**label_de** Position im 3D Modell - Perspektive Position x-Achse    
**label_en** position in 3D model - perspective position x-axis    
**description_de** Kompakkt-spezifische Eigenschaft der Annotationssposition - diese Eigenschaft wird nicht manuell ausgefüllt, sondern nur automatisch, wenn eine neue Annotation gespeichert wird    
**description_en** Kompakkt-specific annotation position property - this property is not meant to be filled out manually, only automatically when a new annotation is saved    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** http://www.w3.org/2001/XMLSchema#float    
**note_en** Wikibase ID: P84, Wikibase datatype: quantity    
### position_in_3d_model_-_perspective_position_y-axis    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/position_in_3d_model_-_perspective_position_y-axis    
**label_de** Position im 3D Modell - Perspektive Position y-Achse    
**label_en** position in 3D model - perspective position y-axis    
**description_de** Kompakkt-spezifische Eigenschaft der Annotationssposition - diese Eigenschaft wird nicht manuell ausgefüllt, sondern nur automatisch, wenn eine neue Annotation gespeichert wird    
**description_en** Kompakkt-specific annotation position property - this property is not meant to be filled out manually, only automatically when a new annotation is saved    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** http://www.w3.org/2001/XMLSchema#float    
**note_en** Wikibase ID: P85, Wikibase datatype: quantity    
### position_in_3d_model_-_perspective_position_z-axis    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/position_in_3d_model_-_perspective_position_z-axis    
**label_de** Position im 3D Modell - Perspektive Position z-Achse    
**label_en** position in 3D model - perspective position z-axis    
**description_de** Kompakkt-spezifische Eigenschaft der Annotationssposition - diese Eigenschaft wird nicht manuell ausgefüllt, sondern nur automatisch, wenn eine neue Annotation gespeichert wird    
**description_en** Kompakkt-specific annotation position property - this property is not meant to be filled out manually, only automatically when a new annotation is saved    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** http://www.w3.org/2001/XMLSchema#float    
**note_en** Wikibase ID: P86, Wikibase datatype: quantity    
### position_in_3d_model_-_perspective_target_x-axis    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/position_in_3d_model_-_perspective_target_x-axis    
**label_de** Position im 3D Modell - Perspektive Ziel x-Achse    
**label_en** position in 3D model - perspective target x-axis    
**description_de** Kompakkt-spezifische Eigenschaft der Annotationssposition - diese Eigenschaft wird nicht manuell ausgefüllt, sondern nur automatisch, wenn eine neue Annotation gespeichert wird    
**description_en** Kompakkt-specific annotation position property - this property is not meant to be filled out manually, only automatically when a new annotation is saved    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** http://www.w3.org/2001/XMLSchema#float    
**note_en** Wikibase ID: P87, Wikibase datatype: quantity    
### position_in_3d_model_-_perspective_target_y-axis    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/position_in_3d_model_-_perspective_target_y-axis    
**label_de** Position im 3D Modell - Perspektive Ziel y-Achse    
**label_en** position in 3D model - perspective target y-axis    
**description_de** Kompakkt-spezifische Eigenschaft der Annotationssposition - diese Eigenschaft wird nicht manuell ausgefüllt, sondern nur automatisch, wenn eine neue Annotation gespeichert wird    
**description_en** Kompakkt-specific annotation position property - this property is not meant to be filled out manually, only automatically when a new annotation is saved    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** http://www.w3.org/2001/XMLSchema#float    
**note_en** Wikibase ID: P88, Wikibase datatype: quantity    
### position_in_3d_model_-_perspective_target_z-axis    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/position_in_3d_model_-_perspective_target_z-axis    
**label_de** Position im 3D Modell - Perspektive Ziel z-Achse    
**label_en** position in 3D model - perspective target z-axis    
**description_de** Kompakkt-spezifische Eigenschaft der Annotationssposition - diese Eigenschaft wird nicht manuell ausgefüllt, sondern nur automatisch, wenn eine neue Annotation gespeichert wird    
**description_en** Kompakkt-specific annotation position property - this property is not meant to be filled out manually, only automatically when a new annotation is saved    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** http://www.w3.org/2001/XMLSchema#float    
**note_en** Wikibase ID: P89, Wikibase datatype: quantity    
### position_in_3d_model_-_selector_ref_normal_x-axis    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/position_in_3d_model_-_selector_ref_normal_x-axis    
**label_de** Position im 3D Modell - Selektor Referenz Normale x-Achse    
**label_en** position in 3D model - selector ref normal x-axis    
**description_de** Kompakkt-spezifische Eigenschaft der Annotationssposition - diese Eigenschaft wird nicht manuell ausgefüllt, sondern nur automatisch, wenn eine neue Annotation gespeichert wird    
**description_en** Kompakkt-specific annotation position property - this property is not meant to be filled out manually, only automatically when a new annotation is saved    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** http://www.w3.org/2001/XMLSchema#float    
**note_en** Wikibase ID: P93, Wikibase datatype: quantity    
### position_in_3d_model_-_selector_ref_normal_y-axis    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/position_in_3d_model_-_selector_ref_normal_y-axis    
**label_de** Position im 3D Modell - Selektor Referenz Normale y-Achse    
**label_en** position in 3D model - selector ref normal y-axis    
**description_de** Kompakkt-spezifische Eigenschaft der Annotationssposition - diese Eigenschaft wird nicht manuell ausgefüllt, sondern nur automatisch, wenn eine neue Annotation gespeichert wird    
**description_en** Kompakkt-specific annotation position property - this property is not meant to be filled out manually, only automatically when a new annotation is saved    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** http://www.w3.org/2001/XMLSchema#float    
**note_en** Wikibase ID: P94, Wikibase datatype: quantity    
### position_in_3d_model_-_selector_ref_normal_z-axis    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/position_in_3d_model_-_selector_ref_normal_z-axis    
**label_de** Position im 3D Modell - Selektor Referenz Normale z-Achse    
**label_en** position in 3D model - selector ref normal z-axis    
**description_de** Kompakkt-spezifische Eigenschaft der Annotationssposition - diese Eigenschaft wird nicht manuell ausgefüllt, sondern nur automatisch, wenn eine neue Annotation gespeichert wird    
**description_en** Kompakkt-specific annotation position property - this property is not meant to be filled out manually, only automatically when a new annotation is saved    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** http://www.w3.org/2001/XMLSchema#float    
**note_en** Wikibase ID: P95, Wikibase datatype: quantity    
### position_in_3d_model_-_selector_ref_point_x-axis    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/position_in_3d_model_-_selector_ref_point_x-axis    
**label_de** Position im 3D Modell - Selektor Referenz Punkt x-Achse    
**label_en** position in 3D model - selector ref point x-axis    
**description_de** Kompakkt-spezifische Eigenschaft der Annotationssposition - diese Eigenschaft wird nicht manuell ausgefüllt, sondern nur automatisch, wenn eine neue Annotation gespeichert wird    
**description_en** Kompakkt-specific annotation position property - this property is not meant to be filled out manually, only automatically when a new annotation is saved    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** http://www.w3.org/2001/XMLSchema#float    
**note_en** Wikibase ID: P90, Wikibase datatype: quantity    
### position_in_3d_model_-_selector_ref_point_y-axis    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/position_in_3d_model_-_selector_ref_point_y-axis    
**label_de** Position im 3D Modell - Selektor Referenz Punkt y-Achse    
**label_en** position in 3D model - selector ref point y-axis    
**description_de** Kompakkt-spezifische Eigenschaft der Annotationssposition - diese Eigenschaft wird nicht manuell ausgefüllt, sondern nur automatisch, wenn eine neue Annotation gespeichert wird    
**description_en** Kompakkt-specific annotation position property - this property is not meant to be filled out manually, only automatically when a new annotation is saved    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** http://www.w3.org/2001/XMLSchema#float    
**note_en** Wikibase ID: P91, Wikibase datatype: quantity    
### position_in_3d_model_-_selector_ref_point_z-axis    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/position_in_3d_model_-_selector_ref_point_z-axis    
**label_de** Position im 3D Modell - Selektor Referenz Punkt z-Achse    
**label_en** position in 3D model - selector ref point z-axis    
**description_de** Kompakkt-spezifische Eigenschaft der Annotationssposition - diese Eigenschaft wird nicht manuell ausgefüllt, sondern nur automatisch, wenn eine neue Annotation gespeichert wird    
**description_en** Kompakkt-specific annotation position property - this property is not meant to be filled out manually, only automatically when a new annotation is saved    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** http://www.w3.org/2001/XMLSchema#float    
**note_en** Wikibase ID: P92, Wikibase datatype: quantity    
### publication_date    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/publication_date    
**label_de** Veröffentlichungsdatum    
**label_en** publication date    
**description_de** Zeitpunkt, zu dem ein bibliografischer Titel veröffentlicht wurde    
**description_en** point in time when a bibliographic item was published    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/bibliographic_work    
**range** http://www.w3.org/2001/XMLSchema#date    
**equivalent property** http://www.wikidata.org/entity/P577, https://schema.org/datePublished    
**note_en** Wikibase ID: P60, Wikibase datatype: edtf    
### ranking    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/ranking    
**label_de** Rang    
**label_en** ranking    
**description_de** Rang, der die Reihenfolge der Anmerkungen im Kompakkt-Walkthrough bestimmt    
**description_en** rank determining the order of annotations in the Kompakkt walkthrough    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/annotation    
**range** http://www.w3.org/2001/XMLSchema#integer    
**note_en** Wikibase ID: P79, Wikibase datatype: quantity    
### reference_url    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/reference_url    
**label_de** Referenz-URL    
**label_en** reference url    
**description_de** URL, in der eine Behauptung aufgestellt wurde – unter Stellungnahme im Feld »Referenzen« zu verwenden    
**description_en** URL where a claim was made - to be used in the references field under a statement    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**range** http://www.w3.org/2001/XMLSchema#string    
**equivalent property** http://www.wikidata.org/entity/P854    
**note_en** Wikibase ID: P56, Wikibase datatype: url    
### start_date    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/start_date    
**label_de** Startdatum    
**label_en** start date    
**description_de** wenn ein Ereignis begonnen hat, auch die Eigenschaft »Enddatum« verwenden (die Eigenschaft »Datum« sollte alternativ verwendet werden, wenn ein Ereignis nur einen Zeitpunkt statt einer Zeitspanne hat)    
**description_en** when an event started, use property 'end date' as well (the property 'date' should be used alternatively when an event only has a point in time instead of a time span)    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/event    
**range** http://www.w3.org/2001/XMLSchema#date    
**equivalent property** http://www.wikidata.org/entity/P580, https://schema.org/startDate    
**note_en** Wikibase ID: P10, Wikibase datatype: edtf    
### surface_area    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/surface_area    
**label_de** Fläche    
**label_en** surface area    
**description_de** Maß    
**description_en** measurement    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**note_en** Wikibase ID: P113, Wikibase datatype: quantity    
### title    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/title    
**label_de** Titel    
**label_en** title    
**description_de** Titel eines kreativen Werks, wenn ausdrücklich angegeben    
**description_en** title of a creative work when explicitly given    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/conceptual_object, https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** http://www.w3.org/2001/XMLSchema#string    
**equivalent property** http://www.wikidata.org/entity/P1476    
**note_en** Wikibase ID: P4, Wikibase datatype: string    
### weight    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/weight    
**label_de** Gewicht    
**label_en** weight    
**description_de** Gewicht eines Objekts    
**description_en** weight of an item    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**subproperty of** https://gitlab.com/nfdi4culture/wikibase4research/model/has_dimension    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** http://www.w3.org/2001/XMLSchema#float    
**equivalent property** http://www.wikidata.org/entity/P2067, https://schema.org/weight    
**note_en** Wikibase ID: P35, Wikibase datatype: quantity    
### width    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/width    
**label_de** Breite    
**label_en** width    
**description_de** Breite eines Objekts    
**description_en** width of an item    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**subproperty of** https://gitlab.com/nfdi4culture/wikibase4research/model/has_dimension    
**domain** https://gitlab.com/nfdi4culture/wikibase4research/model/physical_object    
**range** http://www.w3.org/2001/XMLSchema#float    
**equivalent property** http://www.wikidata.org/entity/P2049, https://schema.org/width    
**note_en** Wikibase ID: P34, Wikibase datatype: quantity    
### wikidata_id    
**iri** https://gitlab.com/nfdi4culture/wikibase4research/model/wikidata_id    
**label_de** Wikidata ID    
**label_en** Wikidata id    
**description_de** Identifikator aus Wikidata    
**description_en** identifier from Wikidata    
**type** http://www.w3.org/2002/07/owl#DatatypeProperty    
**note_en** Wikibase ID: P104, Wikibase datatype: external-id    
