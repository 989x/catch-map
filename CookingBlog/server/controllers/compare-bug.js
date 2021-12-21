/**
 * GET /categories/:id
 * Categories By Id
 */
 exports.exploreCategoriesById = async(req, res) => {

    try {

        let categoryId = req.params.id;
        const limitNumber = 20;
        const categoryById = await Recipe.find({ 'category': categoryId }).limit(limitNumber);

        res.render('categories', {title: 'Cooking Blog - Categories' , categoryById } );
    } catch (error) {
        res.status(500).send({message: error.message || "Error Occured"});
    }
}




/**
 * GET /categories/:id
 * Categories By Id
*/
exports.exploreCategoriesById = async(req, res) => { 
    try {
      let categoryId = req.params.id;
      const limitNumber = 20;
      const categoryById = await Recipe.find({ 'category': categoryId }).limit(limitNumber);
      res.render('categories', { title: 'Cooking Blog - Categoreis', categoryById } );
    } catch (error) {
      res.satus(500).send({message: error.message || "Error Occured" });
    }
  } 