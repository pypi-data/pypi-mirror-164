# quanta
A python library simulating optical circuits.

# ***stokes formalism***

The relationship of the Stokes parameters S0, S1, S2, S3 to intensity and polarization ellipse parameters is shown by:

```
S0 = I
S1 = I*p*cos(2φ)cos(2χ)
S2 = I*p*sin(2φ)sin(2χ)
S3 = I*p*sin(2χ)
```

where:
I : intensity of the polarizer
p : degree of polarization
φ : angle between the major axis of the ellipse and the x-axis
χ : ellipticity angle

Stokes vector is given by: 

S = [S0,S1,S2,S3]

Apart from getting output for specific values there are four common states which are horizontally polarized, vertically polarized, polarized at 45 and -45 degrees.

***Example code***

```
import stokes_formalism from qwanta
print(stokes_formalism.diagonal_positive()) # polarized at 45 degrees
print(stokes_formalism.diagonal_negative()) # polarized at 45 degrees
print(stokes_formalism.horizontal()) # horizontally polarized
print(stokes_formalism.vertical()) # vertically polarized
```