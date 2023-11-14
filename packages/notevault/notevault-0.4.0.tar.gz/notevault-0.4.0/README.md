# NoteVault

Define a schema over markdown documents and store certain sections as columsn in sqlite database.

Every list item must have a `name` as unique key. For non-list items the key is the heading.

## Format
Sections are defined by headings.
Fields (extraction units) correspond to "Tags", e.g. `li, h2`, i.e. `p` should not be a field
because it can contain other tags and newlines.

### Single Item:
- spec: `is_list: false`
- markdown lists as fields: `- key: value`

### Multiple Items:
- spec: `is_list: true`

#### sub-headings
- substructure: format: `## Title x`
can contain:
- markdown lists as fields: `- key: value`
- sub-headings as simple content fields

#### markdown lists
- substructure: format: `- key: value, key: value, key: "complex, value"`
