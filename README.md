# Shader Algorithm Complexity

This tool reads CSV or TXT files, calculates the average of the measures, plots the charts and does the
curve adjustment (also plotting the data). The program is command-line based, having as parameters the shader name
and the measurement used (if it’s related to the whole rendering process or just to the vertex and fragment shaders).

Below its shown two command-lines examples: the first is related to the rendering process of the Gouraud shader
and the second is related only to the vertex and fragment shaders.

$ python  shaderComplexity.py gouraud render_time


$ python  shaderComplexity.py gouraud vertex_fragment

