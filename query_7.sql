SELECT s.name, g.grade
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
JOIN subjects AS sub ON g.subject_id = sub.id
WHERE s.group_id = (SELECT id FROM groups WHERE group_name = 'Певна група')
AND sub.subject_name = 'Певний предмет';