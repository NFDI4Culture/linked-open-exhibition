# Linked Art Ontology — Things (Classes) Reference

> Based on the [Linked Art Data Model 1.0](https://linked.art/model/) — an application profile of [CIDOC-CRM 7.1.3](https://www.cidoc-crm.org/) for describing cultural heritage resources.

## Overview

Linked Art defines a streamlined subset of CIDOC-CRM classes organised into **core entities** (the primary things you describe), **event/activity classes** (things that happen), and **supporting classes** (structures embedded within descriptions). The ontology is serialised as [JSON-LD 1.1](https://linked.art/api/1.0/json-ld/).

---

## 1. Core Entity Classes

These are the primary "things" that receive their own record in the Linked Art API.

| JSON-LD type | CRM Class | Category | Description | Model docs | API endpoint |
|---|---|---|---|---|---|
| `HumanMadeObject` | E22 | Physical Objects | A physical thing made or modified by humans, e.g. a painting, sculpture, or manuscript | [Objects](https://linked.art/model/object/) | [Physical Objects](https://linked.art/api/1.0/endpoint/physical_object/) |
| `DigitalObject` | — (LA extension) | Digital | A born-digital or digitised resource that exists only in computers, e.g. a web page or digital image | [Digital Content](https://linked.art/model/digital/) | [Digital Objects](https://linked.art/api/1.0/endpoint/digital_object/) |
| `Person` | E21 | Agents | An individual human being, e.g. Rembrandt | [People and Organizations](https://linked.art/model/actor/) | [People](https://linked.art/api/1.0/endpoint/person/) |
| `Group` | E74 | Agents | A collective of people capable of acting together, e.g. a museum department, workshop, or married couple | [People and Organizations](https://linked.art/model/actor/) | [Groups](https://linked.art/api/1.0/endpoint/group/) |
| `Place` | E53 | Places | A geographic location, typically with coordinates, e.g. Paris | [Places](https://linked.art/model/place/) | [Places](https://linked.art/api/1.0/endpoint/place/) |
| `Type` | E55 | Concepts | A category, concept, material, technique, or vocabulary term, e.g. "painting" or "oil on canvas" | [Concepts](https://linked.art/model/concept/) | [Concepts](https://linked.art/api/1.0/endpoint/concept/) |
| `Language` | E56 | Concepts | A human language, e.g. English, Dutch | [Concepts](https://linked.art/model/concept/) | (via Concepts) |
| `Material` | E57 | Concepts | A physical material or substance, e.g. oil paint, marble | [Concepts](https://linked.art/model/concept/) | (via Concepts) |
| `MeasurementUnit` | E58 | Concepts | A unit of measurement, e.g. centimetres, inches | [Concepts](https://linked.art/model/concept/) | (via Concepts) |
| `Currency` | E98 | Concepts | A monetary currency, e.g. USD, EUR | [Concepts](https://linked.art/model/concept/) | (via Concepts) |
| `VisualItem` | E36 | Works | The conceptual visual/image content shown by an object, e.g. the image of the Mona Lisa | [Digital Content](https://linked.art/model/digital/) | [Visual Works](https://linked.art/api/1.0/endpoint/visual_work/) |
| `LinguisticObject` | E33 | Works / Documents | Textual content carried by a physical or digital object, e.g. the text of a book | [Textual Documents](https://linked.art/model/document/) | [Textual Works](https://linked.art/api/1.0/endpoint/textual_work/) |
| `PropositionalObject` | E89 | Works | An entirely abstract work that is neither linguistic nor visual, e.g. the notion of an exhibition or performance | [Exhibitions](https://linked.art/model/exhibition/) | [Abstract Works](https://linked.art/api/1.0/endpoint/abstract_work/) |
| `Set` | — (LA extension) | Collections | A set or collection of entities, e.g. a museum collection | [Collections](https://linked.art/model/collection/) | [Sets](https://linked.art/api/1.0/endpoint/set/) |
| `Activity` | E7 | Events | An activity carried out by people or groups, e.g. an exhibition or provenance transfer | [Provenance](https://linked.art/model/provenance/), [Exhibitions](https://linked.art/model/exhibition/) | [Provenance Activities](https://linked.art/api/1.0/endpoint/provenance_activity/) |
| `Period` | E4 | Events | A historical period or era, e.g. the Renaissance | [Events](https://linked.art/model/event/) | [Events](https://linked.art/api/1.0/endpoint/event/) |
| `Event` | E5 | Events | An event that may be depicted or referenced, e.g. a battle | [Events](https://linked.art/model/event/) | [Events](https://linked.art/api/1.0/endpoint/event/) |

---

## 2. Event / Activity Classes

Activities and events model the "what happened" — connecting objects, people, places and time.

| JSON-LD type | CRM Class | Category | Description | Used for |
|---|---|---|---|---|
| `Production` | E12 | Creation | The making of a physical object | Object production |
| `Creation` | E65 | Creation | The creation of a conceptual work (text, image, concept, set) | Works, sets, concepts |
| `Destruction` | E6 | End of existence | The destruction of a physical object | Object destruction |
| `Erasure` | — (LA extension) | End of existence | The erasure/deletion of a digital object | Digital object deletion |
| `Birth` | E67 | Life events | The birth of a person | Person birth |
| `Death` | E69 | Life events | The death of a person | Person death |
| `Formation` | E66 | Group events | The formation of a group or organization | Group formation |
| `Dissolution` | E68 | Group events | The dissolution of a group or organization | Group dissolution |
| `Acquisition` | E8 | Provenance | The acquisition of ownership of an object | Transfer of ownership |
| `TransferOfCustody` | E10 | Provenance | The transfer of physical custody of an object (without ownership change) | Loans, exhibitions |
| `Move` | E9 | Provenance | The physical movement of an object to a new location | Location changes |
| `Modification` | E11 | Conservation | A significant change or modification to an object | Conservation, restoration |
| `PartAddition` | E79 | Conservation | Adding a part to an object | Conservation |
| `PartRemoval` | E80 | Conservation | Removing a part from an object | Conservation, sampling |
| `AttributeAssignment` | E13 | Assertion | Recording a previously held belief or assertion | Specific assertions |
| `Joining` | E85 | Group membership | A person joining a group | Marriage, employment |
| `Leaving` | E86 | Group membership | A person leaving a group | Divorce, retirement |
| `Encounter` | — (LA extension) | Provenance | An encounter with an object (e.g. archaeological find) | Discovery of objects |
| `Payment` | — (LA extension) | Provenance | A payment of money | Auction payments |
| `Right` | E30 | Rights | A right held over an object (appropriated in Linked Art) | Copyright, ownership rights |

---

## 3. Supporting / Embedded Classes

These classes appear as embedded structures within core entity records.

| JSON-LD type | CRM Class | Category | Description | Key properties |
|---|---|---|---|---|
| `Name` | E33_E41 | Identification | A name or appellation for an entity | `content`, `language`, `classified_as` |
| `Identifier` | E42 | Identification | A formal identifier such as an accession number | `content`, `classified_as` |
| `TimeSpan` | E52 | Temporal | A span of time with begin/end dates | `begin_of_the_begin`, `end_of_the_end`, `begin_of_the_end`, `end_of_the_begin` |
| `Dimension` | E54 | Measurement | A measured dimension (height, width, weight, duration, etc.) | `value`, `unit`, `classified_as` |
| `MonetaryAmount` | E97 | Measurement | An amount of money | `value`, `currency` |
| `InformationObject` | E73 | Reference | A reference to an external standard or document | `id`, `type` |

---

## 4. Core Properties (JSON-LD)

These are the key properties used across all Linked Art entities.

| Property | CRM Property | Domain → Range | Description |
|---|---|---|---|
| `id` | — | all → URI | The URI identifying the entity |
| `type` | `rdf:type` | all → Class | The class of the entity |
| `_label` | `rdfs:label` | all → string | Human-readable label for developers |
| `classified_as` | P2 has type | all → Type | Classification using controlled vocabulary (e.g. AAT) |
| `identified_by` | P1 is identified by | all → Name / Identifier | Names and identifiers |
| `referred_to_by` | P67i is referred to by | all → LinguisticObject | Statements and descriptions |
| `equivalent` | — (LA) | all → same class | Links to equivalent resources in other datasets |
| `representation` | — (LA) | all → VisualItem | Image representations |
| `member_of` | P107i is current or former member of | Agent → Group, Entity → Set | Membership in a group or set |
| `part_of` | P46i forms part of | Entity → Entity (same class) | Part–whole relationship |
| `produced_by` | P108i was produced by | HumanMadeObject → Production | Production event |
| `created_by` | P94i was created by | Conceptual → Creation | Creation event |
| `destroyed_by` | P13i was destroyed by | HumanMadeObject → Destruction | Destruction event |
| `born` | P98i was born | Person → Birth | Birth event |
| `died` | P100i died in | Person → Death | Death event |
| `formed_by` | P95i was formed by | Group → Formation | Formation event |
| `dissolved_by` | P99i was dissolved by | Group → Dissolution | Dissolution event |
| `carried_out_by` | P14 carried out by | Activity → Person / Group | Who performed an activity |
| `took_place_at` | P7 took place at | Event → Place | Where something happened |
| `timespan` | P4 has time-span | Event → TimeSpan | When something happened |
| `during` | — (LA) | Event → Period | Period during which an event occurred |
| `used_specific_object` | P16 used specific object | Activity → HumanMadeObject | Object used in an activity |
| `technique` | P32 used general technique | Activity → Type | Technique or method used |
| `carries` | P128 carries | HumanMadeObject → LinguisticObject | Textual content on an object |
| `shows` | P65 shows visual item | HumanMadeObject → VisualItem | Visual content on an object |
| `about` | P129 is about | Work → any entity | Subject matter |
| `represents` | P138 represents | VisualItem → any entity | What is depicted |
| `content` | P190 has symbolic content | LinguisticObject / Name / Identifier → string | The textual value |
| `language` | P72 has language | LinguisticObject → Language | Language of text |
| `format` | dc:format | LinguisticObject / DigitalObject → string | Media type (e.g. "text/html") |
| `value` | P90 has value | Dimension → number | Numeric measurement value |
| `unit` | P91 has unit | Dimension → MeasurementUnit | Unit of measurement |
| `currency` | — (LA) | MonetaryAmount → Currency | Currency of a monetary amount |
| `begin_of_the_begin` | P82a | TimeSpan → xsd:dateTime | Earliest possible start |
| `end_of_the_end` | P82b | TimeSpan → xsd:dateTime | Latest possible end |
| `current_owner` | P52 has current owner | HumanMadeObject → Person / Group | Current owner |
| `current_location` | P55 has current location | HumanMadeObject → Place | Current location |
| `made_of` | P45 consists of | HumanMadeObject → Material | Material composition |
| `dimension` | P43 has dimension | HumanMadeObject → Dimension | Measured dimensions |
| `access_point` | — (LA) | DigitalObject → DigitalObject | Downloadable file URL |
| `digitally_carries` | — (LA) | DigitalObject → LinguisticObject | Text in a digital object |
| `digitally_shows` | — (LA) | DigitalObject → VisualItem | Image in a digital object |
| `conforms_to` | P2 has type (refinement) | DigitalObject → InformationObject | Standard the digital object conforms to |

---

## 5. Model Sections Summary

| Section | Description | Documentation |
|---|---|---|
| Objects | Physical things: production, destruction, physical characteristics, aboutness, ownership, rights | [Objects](https://linked.art/model/object/) |
| Digital Content | Digital representations of or about physical objects | [Digital](https://linked.art/model/digital/) |
| Collections | Sets and collections of objects and other entities | [Collections](https://linked.art/model/collection/) |
| Provenance | Ownership history: acquisitions, loans, auctions, custody, encounters, movement, promises, rights transfer | [Provenance](https://linked.art/model/provenance/) |
| Exhibitions | Exhibition events and the objects exhibited | [Exhibitions](https://linked.art/model/exhibition/) |
| Conservation | Modification, part addition/removal, and condition of objects | [Conservation](https://linked.art/model/conservation/) |
| People and Organizations | Persons and groups: birth/death, formation/dissolution, membership | [Actors](https://linked.art/model/actor/) |
| Places | Geographic locations, coordinates, hierarchies | [Places](https://linked.art/model/place/) |
| Concepts | Types, vocabularies, materials, techniques, languages, units | [Concepts](https://linked.art/model/concept/) |
| Events | Historical periods and events | [Events](https://linked.art/model/event/) |
| Textual Documents | Textual works and documents | [Documents](https://linked.art/model/document/) |
| Archival Hierarchies | Archival arrangement and description | [Archives](https://linked.art/model/archives/) |
| Specific Assertions | Previously held beliefs and attribute assignments | [Assertions](https://linked.art/model/assertion/) |

---

## 6. API Endpoints

| Endpoint | Entity Type | URL |
|---|---|---|
| Physical Objects | `HumanMadeObject` | [/api/1.0/endpoint/physical_object/](https://linked.art/api/1.0/endpoint/physical_object/) |
| Digital Objects | `DigitalObject` | [/api/1.0/endpoint/digital_object/](https://linked.art/api/1.0/endpoint/digital_object/) |
| People | `Person` | [/api/1.0/endpoint/person/](https://linked.art/api/1.0/endpoint/person/) |
| Groups | `Group` | [/api/1.0/endpoint/group/](https://linked.art/api/1.0/endpoint/group/) |
| Places | `Place` | [/api/1.0/endpoint/place/](https://linked.art/api/1.0/endpoint/place/) |
| Concepts | `Type`, `Language`, `Material`, `MeasurementUnit`, `Currency` | [/api/1.0/endpoint/concept/](https://linked.art/api/1.0/endpoint/concept/) |
| Visual Works | `VisualItem` | [/api/1.0/endpoint/visual_work/](https://linked.art/api/1.0/endpoint/visual_work/) |
| Textual Works | `LinguisticObject` | [/api/1.0/endpoint/textual_work/](https://linked.art/api/1.0/endpoint/textual_work/) |
| Abstract Works | `PropositionalObject` | [/api/1.0/endpoint/abstract_work/](https://linked.art/api/1.0/endpoint/abstract_work/) |
| Sets | `Set` | [/api/1.0/endpoint/set/](https://linked.art/api/1.0/endpoint/set/) |
| Events | `Period`, `Event` | [/api/1.0/endpoint/event/](https://linked.art/api/1.0/endpoint/event/) |
| Provenance Activities | `Activity` | [/api/1.0/endpoint/provenance_activity/](https://linked.art/api/1.0/endpoint/provenance_activity/) |

---

## References

- Linked Art website: <https://linked.art/>
- Data Model 1.0: <https://linked.art/model/>
- API 1.0: <https://linked.art/api/1.0/>
- Profile (CIDOC-CRM subset): <https://linked.art/model/profile/>
- Class Analysis: <https://linked.art/model/profile/class_analysis/>
- JSON-LD Context: <https://linked.art/ns/v1/linked-art.json>
- Linked Art Ontology (additional terms): <https://linked.art/ns/terms/>
- CIDOC-CRM: <https://www.cidoc-crm.org/>
- Getty AAT: <http://vocab.getty.edu/aat/>

---

*Generated from the Linked Art 1.0 specification on 2026-04-15.*
