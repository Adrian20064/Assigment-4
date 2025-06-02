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

            # Validaciones personalizadas
            if not all(isinstance(x, (int, float)) for x in [a, b, c]):
                error = "Todos los valores deben ser numéricos."
            elif a < 1:
                error = "El valor de 'a' es demasiado pequeño. Debe ser mayor o igual a 1."
            elif c < 0:
                error = "El valor de 'c' no puede ser negativo."
            else:
                c_cubed = c ** 3
                calculation_result = 0

                if c_cubed > 1000:
                    calculation_result = math.sqrt(c_cubed) * 10
                else:
                    try:
                        calculation_result = math.sqrt(c_cubed) / a
                    except ZeroDivisionError:
                        error = "División por cero en la operación con 'a'."

                if not error:
                    calculation_result += b
                    if b == 0:
                        message = "Nota: 'b' es 0, no afectará el resultado."
                else:
                    message = "Cálculo completado exitosamente."

                    result = f"""
                        <h2>Resultado</h2>
                        <p><strong>Valor de a:</strong> {a}</p>
                        <p><strong>Valor de b:</strong> {b}</p>
                        <p><strong>Valor de c:</strong> {c}</p>
                        <p><strong>c³:</strong> {c_cubed}</p>
                        <p><strong>Resultado final:</strong> {calculation_result:.2f}</p>
                        <p>{message}</p>
                    """
        else:
            error = "Formulario no válido. Verifica los campos."
    else:
        form = InputForm()

    return render(request, 'calculator/result.html', {'form': form, 'result': result, 'error': error})

