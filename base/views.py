from django.shortcuts import render
import math

def index(request):
    result = {}
    if request.method == "POST":
        try:
            velocity = float(request.POST.get("velocity"))
            energy = float(request.POST.get("energy"))
            unit = request.POST.get("unit")
            weights_raw = request.POST.get("weights")

            # Convert velocity
            mps = velocity * 0.3048 if unit == "fps" else velocity

            # Time to fall from 1m
            t = math.sqrt(2 / 9.81)

            # Parse weights list
            weights = [float(w.strip()) for w in weights_raw.split(",") if w.strip()]
            table = []

            for w in weights:
                # Recalculate velocity for this weight using E = 0.5 * m * v^2 → v = sqrt(2E/m)
                v_mps = math.sqrt((2 * energy) / (w / 1000))
                range_m = v_mps * t
                table.append({
                    "weight": round(w, 2),
                    "mps": round(v_mps, 2),
                    "fps": round(v_mps / 0.3048, 2),
                    "range_m": round(range_m, 2),
                    "range_ft": round(range_m * 3.281, 2)
                })

            result["table"] = table
            result["velocity"] = round(mps, 2)
            result["energy"] = round(energy, 3)

        except Exception as e:
            result["error"] = f"Error: {str(e)}"

    return render(request, "index.html", {"result": result})
