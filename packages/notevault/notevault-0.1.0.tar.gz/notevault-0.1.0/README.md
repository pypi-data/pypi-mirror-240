# vimania-sqlite

bash script to create a sqlite database from vimania's csv files,
```bash
sqlite-utils query semantic_units.db "
SELECT 
    document.name,
    general.start,
    general.end,
    general.breaks,
    general.timestamp,
    general.date,
    meeting.name AS meeting_name,
    meeting.start AS meeting_start,
    meeting.duration,
    meeting.minutes,
    meeting.participants
FROM document
LEFT JOIN general ON document.name = general.document_name
LEFT JOIN meeting ON document.name = meeting.document_name;
"

```
