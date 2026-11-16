const express = require('express');
const { Pool } = require('pg');

const app = express();
const pool = new Pool({
  host: 'db',
  user: process.env.POSTGRES_USER,
  password: process.env.POSTGRES_PASSWORD,
  database: process.env.POSTGRES_DB,
  port: 5432,
});

app.get('/', async (req, res) => {
  try {
    const result = await pool.query('SELECT NOW()');
    res.json({ status: 'ok', servicio: 'node', hora_db: result.rows[0].now });
  } catch (err) {
    res.status(500).json({ status: 'error', detalle: err.message });
  }
});

app.listen(3000, () => console.log('Node app escuchando en puerto 3000'));