"""The editable examples reproduce the presentation on the same sample."""
import importlib.util
import gzip
import sys
from io import BytesIO
from pathlib import Path
from unittest.mock import patch

import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "practice"))
csv_spec = importlib.util.spec_from_file_location("data_io", ROOT / "practice/data_io.py")
data_io = importlib.util.module_from_spec(csv_spec)
csv_spec.loader.exec_module(data_io)
# A browser decodes Content-Encoding before Python sees the response body.
for body in [b"x,y\n1,2\n", gzip.compress(b"x,y\n1,2\n")]:
    response = BytesIO(body)
    response.headers = {"Content-Encoding": "gzip"}
    with patch.object(data_io, "urlopen", return_value=response):
        assert data_io.read_csv("https://example.test/data.csv").iloc[0].tolist() == [1, 2]
assert len(data_io.read_csv(ROOT / "practice/data/chap1-stand_data.csv")) == 2400
print("PASS: CSV loading for local files, browser-decoded HTTP, and compressed HTTP")

spec = importlib.util.spec_from_file_location(
    "regression_lab", ROOT / "practice/regression_lab.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
_, state = module.app.run()
assert int(state["ols_fit"].nobs) == 2400
assert len(state["air_sample"]) == int(state["logit_fit"].nobs) == 4259
assert state["logit_fit"].mle_retvals["converged"]
assert np.isfinite(state["logit_ame"].to_numpy()).all()

# A code edit changes the fitted model while keeping the data fixed.
_, changed = module.app.run(defs={
    "ols_formula": "icecream_sales ~ temps + summer_months + iced_coffee_sales",
    "logit_formula": "bkd ~ ad",
})
assert set(changed["ols_fit"].params.index) == {
    "Intercept", "temps", "summer_months", "iced_coffee_sales"
}
assert abs(changed["ols_fit"].params["temps"] - 2702.788) < .001
assert int(changed["logit_fit"].nobs) == 4259
mean_difference = changed["air_sample"].groupby("ad")["bkd"].mean().diff().iloc[-1]
assert abs(changed["logit_ame"].loc["ad", "dy/dx"] - mean_difference) < 1e-8
print("PASS: editable OLS/logit examples, fixed comparison sample, convergence, and AME")
