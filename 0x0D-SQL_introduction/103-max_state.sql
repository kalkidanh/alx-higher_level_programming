-- Display the maximum temperature of every state in order.
SELECT state, max(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
