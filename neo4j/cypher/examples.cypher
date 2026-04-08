// Example 1
// -- Find all movies
MATCH (m:Movie)
RETURN m.title, m.released
ORDER BY m.released;

// Example 2
// -- Find all actors in "The Matrix"
MATCH (a:Person)-[:ACTED_IN]->(m:Movie {title: "The Matrix"})
RETURN a.name