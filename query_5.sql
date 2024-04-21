SELECT sub.subject_name
FROM teachers AS t
JOIN subjects AS sub ON t.id = sub.teacher_id
WHERE t.teacher_name = 'Певний викладач';