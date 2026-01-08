# app/api/routes.py
@app.route("/predict", methods=["POST"])
def predict():
    image = request.files["image"]
    tensor = preprocess(image)
    preds = run_inference(tensor, model)
    risk = compute_risk(preds)
    return jsonify({"risk_score": risk})