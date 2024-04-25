const mongoose = require('mongoose');
const Sede = require('./models/sede');
const Rol = require('./models/rol');
const Usuario = require('./models/usuario');

mongoose.connect('mongodb+srv://javierposso:dbb1998@cluster0.oxkhfvu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(async () => {
  console.log('Conexión a MongoDB establecida');

  // Crear sedes
  const sedes = [
    { nombreSede: 'Medellin' },
    { nombreSede: 'Cali' },
    { nombreSede: 'Bogota' }
  ];

  await Sede.insertMany(sedes);

  console.log('Sedes creadas con éxito');

  // Crear roles
  const roles = [
    { nombreRol: 'Cliente' },
    { nombreRol: 'Vendedor' },
    { nombreRol: 'Gerente' }
  ];

  await Rol.insertMany(roles);

  console.log('Roles creados con éxito');

  // Obtener una sede y un rol existente para el usuario
  const sedeSeleccionada = await Sede.findOne({ nombreSede: 'Cali' });
  const rolSeleccionado = await Rol.findOne({ nombreRol: 'Gerente' });

  // Crear el usuario
  const nuevoUsuario = new Usuario({
    nombre: 'Gerente',
    apellido: 'Diaz',
    telefono: '3137855322',
    email: 'gerentediaz@correo.com',
    nombreSede: sedeSeleccionada._id,
    contraseña: '1234',
    nombreRol: rolSeleccionado._id
  });

  await nuevoUsuario.save();

  console.log('Usuario creado con éxito');
})
.catch(err => console.error('Error al conectar a MongoDB:', err));
