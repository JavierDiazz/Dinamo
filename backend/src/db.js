const mongoose = require('mongoose');

const MONGODB_URI = 'mongodb+srv://javierposso:dbb1998@cluster0.oxkhfvu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0';

mongoose.connect(MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('Conexión a MongoDB establecida'))
.catch(err => console.error('Error al conectar a MongoDB:', err));
