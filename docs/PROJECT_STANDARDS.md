# Project Standards

- Use stable descriptive machine paths and preserve technically meaningful original identifiers.
- Record version/language/revision/region/update/form distinctions when material.
- Prefer editable source and reproducible generation steps; never invent unknown metadata.
- Separate confirmed observations from hypotheses; prefer hashes and stable IDs over filenames alone.
- Reviewable previews are allowed; deduplicate only after byte/hash confirmation.
- Keep one live structure. No repository-wide `vN`, `PRE-VN`, `MIGRATED`, or parallel legacy trees. Git history is the historical layer.
- Every project/artifact has one canonical home; indexes may reference it without competing ownership.
- Never commit retail or rebuilt ROMs, complete decrypted game images, keys, or disguised complete images.

Platform-specific rules may extend these standards only after the architecture is verified.