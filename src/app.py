from flask import Flask, render_template, request
from prediction.predict import predict_bug

app = Flask(
    __name__,
    template_folder="../templates"
)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    confidence = None
    risk = None

    if request.method == "POST":

        loc = float(request.form["loc"])
        vg = float(request.form["vg"])
        evg = float(request.form["evg"])
        branch_count = float(request.form["branch_count"])
        total_op = float(request.form["total_op"])

        prediction, confidence, risk = predict_bug(
            loc,
            vg,
            evg,
            branch_count,
            total_op
        )

        if prediction == 1:
            result = "Buggy Module"
        else:
            result = "Non-Buggy Module"

    return render_template(
        "index.html",
        result=result,
        confidence=confidence,
        risk=risk
    )


if __name__ == "__main__":
    app.run(debug=True)