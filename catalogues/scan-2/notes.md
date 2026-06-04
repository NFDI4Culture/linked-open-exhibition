# Open Questions — baldessari-sprengel extraction

## Target Wikibase instance
The project documents reference `wbworkshop.tibwiki.io` as the upload target, but that instance was unreachable at time of writing. Options when ready to upload:
- Upload to the TIB workshop Wikibase (if it comes back online)
- Upload directly to Wikidata (requires community vetting)
- Stand up a local Wikibase instance for prototyping

Not blocking for local extraction prototype — all three plans output standard Wikidata P-number CSV that works with any QuickStatements-compatible endpoint.

## WB4R local P-numbers vs. Wikidata P-numbers
The WB4R (Wikibase4Research) instance uses its own local property IDs (P1–P137) that do NOT match Wikidata property IDs. All three plans currently use Wikidata P-numbers (P31, P170, P1476, etc.) as column headers. If the final upload target is the WB4R instance rather than Wikidata, column headers will need remapping via the `wikibase_generic_model.csv` alignment table in the GitHub repo.

## Verify P1431 = Q138573075
Q138573075 was cited in the NFDI4Culture exhibition data model page as the Sprengel Museum exhibition Q-ID, but this should be verified against Wikidata before upload. Could be a workshop/sandbox Q-ID rather than a live Wikidata item.
