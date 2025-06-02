from django.shortcuts import render
from .forms import InputForm
import math

def calculate_view(request):
    result = None
    error = None

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            if not all(isinstance(x, (int, float)) for x in [a, b, c]):
                error = "All values must be numeric."
            elif a < 1:
                error = "The value of 'a' is too small. It must be at least 1."
            elif c < 0:
                error = "The value of 'c' cannot be negative."
            else:
                c_cubed = c ** 3
                calculation_result = 0

                if c_cubed > 1000:
                    calculation_result = math.sqrt(c_cubed) * 10
                else:
                    try:
                        calculation_result = math.sqrt(c_cubed) / a
                    except ZeroDivisionError:
                        error = "Division by zero occurred with 'a'."

                if not error:
                    calculation_result += b
                    if b == 0:
                        message = "Note: 'b' is 0 and won't affect the result."
                    else:
                        message = "Calculation completed successfully."

                    result = f"""
                        <h2>Result</h2>
                        <p><strong>Value of a:</strong> {a}</p>
                        <p><strong>Value of b:</strong> {b}</p>
                        <p><strong>Value of c:</strong> {c}</p>
                        <p><strong>c³:</strong> {c_cubed}</p>
                        <p><strong>Final result:</strong> {calculation_result:.2f}</p>
                        <p>{message}</p>
                    """
        else:
            error = "Invalid form. Please check your input."
    else:
        form = InputForm()

    return render(request, 'calculator/result.html', {'form': form, 'result': result, 'error': error})
