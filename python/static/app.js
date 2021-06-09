document.addEventListener("DOMContentLoaded", () => {
  // va chercher tous les éléments avec la classe "column"
  const $columns = document.querySelectorAll(".column");

  // pour chacun de ses éléments
  $columns.forEach((column) => {
    // on va lire l'attribut "data-target"
    const target = column.dataset.target;
    column.addEventListener("click", () => {
      // on ajoute un handler avec cette target
      console.log(`Vous avez cliqué sur l'image ${target} à ${Date.now()}`);
      // location.reload();
    });
    console.info(`Handler enregistré pour ${target}`);
  });
  console.info("Document complètement chargé");
});
