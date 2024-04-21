SELECT g.group_name, AVG(gg.grade) AS average_grade
FROM groups AS g
JOIN students AS s ON g.id = s.group_id
JOIN grades AS gg ON s.id = gg.student_id
JOIN subjects AS sub ON gg.subject_id = sub.id
WHERE sub.subject_name = 'Певний предмет'
GROUP BY g.id;