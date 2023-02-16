import conexion from '../conector_bd.js'

export const crearProducto = async (req,res)=>{
    const{body}=req
    // primero buscar si existe la categoria
    const categoria =await conexion.categoria.findFirst({where:{id:+body.categoria}})

    // si no existe retornar un mensaje que los datos son incorrectos
    if (!categoria){
        return res.json({
            message : 'la categoria no existe',
        })
    }
    const resultado = await conexion.producto.create({
        data: {
            ...body,
            categoriaId:+body.categoriaId,
        },
    })
    return res.json({
        message:'Producto creado exitosamente',
        content: resultado,

    })

}