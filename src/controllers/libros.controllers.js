export const agregarLibro = (req, res) => {
  const data = req.body;
  console.log(req.user);
  return res.json({
    message: "ok",
  });
};
