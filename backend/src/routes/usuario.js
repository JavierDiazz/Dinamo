const express = require('express');
const router = express.Router();
const bcrypt = require('bcrypt');
const Usuario = require('../models/usuario');

// Obtener todos los usuarios
router.get('/', async (req, res) => {
  try {
    const usuarios = await Usuario.find();
    res.json(usuarios);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Obtener un usuario por ID
router.get('/:id', getUsuario, (req, res) => {
  res.json(res.usuario);
});

// Ruta para iniciar sesión
router.post('/login', async (req, res) => {
  const { email, contraseña } = req.body;

  try {
    // Buscar el usuario por email
    const usuario = await Usuario.findOne({ email });

    if (!usuario) {
      return res.status(401).json({ message: 'Credenciales incorrectas' });
    }

    // Verificar la contraseña
    if (!(await bcrypt.compare(contraseña, usuario.contraseña))) {
      return res.status(401).json({ message: 'Credenciales incorrectas' });
    }

    // Enviar una respuesta exitosa
    res.status(200).json({ message: 'Inicio de sesión exitoso' });
  } catch (error) {
    console.error('Error al iniciar sesión:', error);
    res.status(500).json({ message: 'Error interno del servidor' });
  }
});

// Crear un nuevo usuario
router.post('/', async (req, res) => {
  const usuario = new Usuario({
    _id: req.body.id,
    nombre: req.body.nombre,
    apellido: req.body.apellido,
    telefono: req.body.telefono,
    email: req.body.email,
    nombreSede: req.body.nombreSede,
    contraseña: req.body.contraseña,
    nombreRol: req.body.nombreRol
  });

  try {
    const nuevoUsuario = await usuario.save();
    res.status(201).json(nuevoUsuario);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// Actualizar un usuario por ID
router.patch('/:id', getUsuario, async (req, res) => {
  if (req.body.nombre != null) {
    res.usuario.nombre = req.body.nombre;
  }
  if (req.body.apellido != null) {
    res.usuario.apellido = req.body.apellido;
  }
  if (req.body.telefono != null) {
    res.usuario.telefono = req.body.telefono;
  }
  if (req.body.email != null) {
    res.usuario.email = req.body.email;
  }
  if (req.body.nombreSede != null) {
    res.usuario.nombreSede = req.body.nombreSede;
  }
  if (req.body.contraseña != null) {
    res.usuario.contraseña = req.body.contraseña;
  }
  if (req.body.nombreRol != null) {
    res.usuario.nombreRol = req.body.nombreRol;
  }

  try {
    const usuarioActualizado = await res.usuario.save();
    res.json(usuarioActualizado);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// Eliminar un usuario por ID
router.delete('/:id', getUsuario, async (req, res) => {
  try {
    await res.usuario.remove();
    res.json({ message: 'Usuario eliminado' });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

async function getUsuario(req, res, next) {
  try {
    usuario = await Usuario.findById(req.params.id);
    if (usuario == null) {
      return res.status(404).json({ message: 'Usuario no encontrado' });
    }
  } catch (err) {
    return res.status(500).json({ message: err.message });
  }

  res.usuario = usuario;
  next();
}

module.exports = router;
