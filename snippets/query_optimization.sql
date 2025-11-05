-- Ejemplo de optimización de consulta (no propietario)
-- Antes: SELECT * FROM products WHERE name LIKE '%texto%'
-- Después: índice en LOWER(name) y búsqueda normalizada
CREATE INDEX IF NOT EXISTS idx_products_lower_name ON products(LOWER(name));
-- SELECT * FROM products WHERE LOWER(name) LIKE LOWER('%texto%');
