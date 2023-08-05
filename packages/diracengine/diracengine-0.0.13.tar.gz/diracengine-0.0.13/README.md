# <span style="background: linear-gradient(2deg, #3d4cff 0%, #ff3bd8 100%); -webkit-text-fill-color: transparent;-webkit-background-clip: text;">**The Dirac Quantum Engine**: ***a tribute to a legend***</span>

<p align="center"><image src="./assets/dirac_engine.svg" width=20% /></p>

## Contents

0. [A Tribute to a Legend](#a-tribute-to-a-legend)
1. [Let's Get Started](#lets-get-started)
    * [Requirements](#requirements)
    * [Installation](#installation)
    * [Importing the engine](#importing-the-engine)
2. [Hello Quantum World](#hello-quantum-world)
    * [The Qubit](#the-qubit)
    * [Spin 1/2](#spin-12)
    * [The Wave Function](#the-wave-function)
    * [The Schrödinger equation](#the-schrödinger-equation)

---

## **A Tribute to a Legend**

The **Dirac engine** is a *Pyhon physics engine* which simulates quantum phenomena. This includes basic quantum and wave mechanics, [spin 1/2 particles](https://en.wikipedia.org/wiki/Spin-1/2) and their antimatter partners.

In 1928 [**Paul Dirac**](https://en.wikipedia.org/wiki/Paul_Dirac), an english physicist, was working on a relativistic theory of quantum mechanics. The result is a beautiful equation:

$$ i \hbar \gamma^\mu \partial_\mu \ket\psi - m c \ket\psi = 0 $$

This equation predicts electron spin, the periodic table, antimatter and the **g** factor. It is also the first building block of [**quantum field theory**](https://en.wikipedia.org/wiki/Quantum_field_theory): оur best description of reality (yet).

This equation is the core of the **Dirac engine**. This is why this name has been chosen for the project. The engine is *a tribute to a legend*: **Paul Dirac**, one of the geniuses of the 20th century.

[<p align="center"><image src="./assets/paul_dirac_gradient.png" width=30% /></p>](https://en.wikipedia.org/wiki/Paul_Dirac)

Quantum field theory is hard. It requires years of studying just for the basics. But that is not the main problem. Calculations in quantum field theory are beyond the performance limits of modern computers. So, how could we simulate the quantum realm?

Fortunately, quantum field theory's predecessor: [**quantum mechanics**](https://en.wikipedia.org/wiki/Quantum_mechanics), is easier. It does not require you to build a cluster of supercomputers. You can simulate basic quantum phenomena on your own computer.

---

## **Let's Get Started**

### **Requirements**

Let's get started with the engine. Firstly: the **requirement**. Using this engine is not for everyone. But if you have passed the requirements you will not have any problems when coding. Here are they:

* **Python**: *it is obvious*

* **basic quantum mechanics**: *don't worry, we have provided an [introduction guide to quantum mechanics]()*

* **linear algebra**: *this is Python so you should be good*

* **complex numbers**: *√-1 is possible*

* **hamiltonian mechanics**: *if you know this, you can skip the other*

* **multivariable calculus**: *just the basics*

* **basic physics**: *this is a must*

### **Installation**

If you are comfortable with most of the requirements, you can proceed to the **installation**. You can install it like any other PIP package. Just open your terminal and paste this command:

```console
pip install diracengine
```

Congratulations! You have installed the **Dirac engine**.

### **Importing the engine**

Now let's import the package in Python. Open a new .py flie and write:

```python
import diracengine as dirac
```

This is it. You are ready to use the **Dirac engine**. In the next chapter we will write our first dirac programs. By the end of the chapter you will be able to solve the **Schrodinger equation** on your own with just a few lines of code.

## **Hello *Quantum* World**

In this chapter we will show you how to code with the **Dirac engine**. We will start with the basics. Then we will progress to more advanced cases. In this chapter we will figure:

**1. Quantum state**

* [**Quantum bits**](#the-qubit): a great introduction to the building blocks of quantum computing

* [**Spin 1/2**](#spin-12): meeting our first quantum operators

**2. Wave function**:

* [**Continuous quantum states**](#the-wave-function): how to discretize continuous funtions

* [**The Schrödinger equation**](#the-schrödinger-equation): time evolution of the wave function

> Note: We will be using [Dirac's bra-ket notation](https://en.wikipedia.org/wiki/Bra–ket_notation) from now on. If you are not comfortable with it, you can check our [introduction guide to quantum mechanics]().

### **The Qubit**

Our first example will be a [quantum bit](https://en.wikipedia.org/wiki/Qubit), shortly a **qubit**. A qubit is a quatum object with two states: 0 or 1. The qubit is in a **superposition** of both states. Each state has some **probability amplitude**. We can express this mathematically:

$$ \ket\psi = \alpha\ket0 + \beta\ket1 $$

where $\alpha$ is the probability amplitude of the 0 state and $\beta$: the 1 state. This quatum state will look like this:

```python
import diracengine as dirac

psi = dirac.QuantumState([ alpha, beta ], [ 0, 1 ])
```

The ``QuantumState`` object is initiated when two arguments are provided: ``probabilityAmplitudes`` and ``basis``. They must be lists. ``probabilityAmplitudes`` must include complex numbers only while ``basis`` does not have restrictions.

Let's try to initiate a qubit with equally likely possibilities of being 0 or 1:

$$ \ket\psi = \alpha\ket0 + \alpha\ket1 $$

In the language of the **Dirac engine** this will look like this:

```python
import diracengine as dirac

alpha = 1 + 0j

psi = dirac.QuantumState([ alpha, alpha ], [ 0, 1 ])
```

But there is an issue. In quantum mechanics the quantum state **must be normalized**:

$$ \braket{\psi|\psi} = 1 $$

This means that if we want a normalized quantum state we need $\alpha$ to be:

$$ \alpha^*\alpha = \frac{1}{2} $$

If we assume that $\alpha$ is a real number: $\alpha \in \mathbb{R}$, this means that $\alpha$ must be $\pm \sqrt{\frac{1}{2}}$, not 1. So, we have made a mistake?

The **Dirac engine normalizes the quantum state by default**. It only scales the probability amplitudes, preserving their phase. This means that when we pass $\alpha = 1$, the engine will convert it to  $\alpha = \sqrt{\frac{1}{2}}$. We can test this by printing the quantum state:

```python
import diracengine as dirac

alpha = 1 + 0j

psi = dirac.QuantumState([ alpha, alpha ], [ 0, 1 ])

print(psi)
```

The terminal output is:

```console
[
        0: 0.7071067811865476 + 0.0i 
        1: 0.7071067811865476 + 0.0i 
]
```

> **Tip**: if you want to work with **unnormalized** probability amplitudes you can change the ``normalize`` argument to ``False`` when initiating the object:
> ```python
> psi = dirac.QuantumState(probabilityAmplitudes, basis, normalize = False)
>```
> You can also change ``norm`` of the state $\braket{\psi|\psi}$. By default it is set to 1.
> ```python
> norm = 1
> psi = dirac.QuantumState(probabilityAmplitudes, basis, norm = norm)
> ```

Let's return to the general case. We will try an arbitrary value for $\beta$. For example let $\beta$ be $i$:

```python
import diracengine as dirac

alpha = 1 + 0j
beta = 0 + 1j

psi = dirac.QuantumState([ alpha, beta ], [ 0, 1 ])

print(psi)
```

```console
[
        0: 0.7071067811865476 + 0.0i
        1: 0.0 + 0.7071067811865476i
]
```

We can see that $\beta$ is still an imaginary number after the normalization. The phase of $\beta$ looks the same. We can test this. We can get the new value for $\beta$ after the normalization like this:

```python
psi.probabilityAmplitude(1)
```

Now we will import the ``cmath`` module to get the phase of the complex number. Then we will print the results on the terminal.

```python
import cmath
import diracengine as dirac

alpha = 1 + 0j
beta = 0 + 1j

psi = dirac.QuantumState([ alpha, beta ], [ 0, 1 ])

newBeta = psi.probabilityAmplitude(1)

phaseBeta = cmath.phase(beta)
phaseNewBeta = cmath.phase(newBeta)

print(phaseBeta, phaseNewBeta)
```

```console
1.5707963267948966 1.5707963267948966
```

The result is 90° in radians. Just to remind you, you can convert to degrees by multiplying by $180^\circ/\pi$.

Our next goal will be converting the complex **probability amplitudes** to real **probabilities**. We can get the probability of a base state with this method:

```python
psi.probability(base)
```

In this case for the states 0 and 1 we get ``0.5``. The states are equally likely.

You can get the total quantum state's probability. If you haven't touched ``normalize`` and ``norm`` attributes you should always get 1. Just use the ``totalProbability`` method:

```python
psi.totalProbability()
```

There are other useful methods. If you want to see all the methods go to the ...

This concludes our qubit tour. In the next section we will get familiar with **quantum operators** in the **Dirac engine**.

### **Spin 1/2**

The **electron** is famous for its **two-valuesness**. It behaves like a qubit. The two states are called: **spin-up** and **spin-down**.:

$$ \ket\psi = \alpha\ket\uparrow + \beta\ket\downarrow $$

Now let's use the **Dirac engine** to create an electron:

```python
import diracengine as dirac

alpha = 1 + 0j
beta = 0 + 1j

basis = [ 'spin-up', 'spin-down' ]

psi = dirac.QuantumState([ alpha, beta ], basis)
```

All fermions that have this qubit-like property are classified as **spin 1/2 particles**. Spin is a fundamental property of nature. It does not have a classical analog. It is a pure quantum property. Spin seems like intrinsic angular momentum. In fact, it is its origin. But if this were true, spin would violate relativity. That is why spin doesn't mean spinning.

We can measure this "angular momentum" property. We can use a **quantum operator** for this job. Operators measure properties. For example, we can measure the spin of the electron by applying the spin operator to the state.

Before we start coding, we should look at some examples. Let's calculate the spin of 100% spin-up particle. If we measure the spin we should get $\hbar/2$:

$$ \hat{S}\ket{\uparrow} = \frac{\hbar}{2}\ket{\uparrow} $$

And if we do this for spin-down spin must be negative, because it is "spinning" in the opposite direction:

$$ \hat{S}\ket{\downarrow} = - \frac{\hbar}{2} \ket{\downarrow} $$

Those two equation are also called: eigenstate equations. We can solve those equations for the spin operator:

$$ \hat{S} = \frac{\hbar}{2} \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} $$

Now we can apply this operator for an arbitrary quantum state to measure how much the electron is "spining" up or down:

$$ \hat{S}\ket\psi = \frac{\hbar}{2} \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \begin{bmatrix} \alpha \\ \beta \end{bmatrix} $$

Let's compute this. We will use natiral units: $\hbar = 1$. Firstly, we need to create the matrix. We will use the ``numpy`` library:

```python
import numpy

spinMatrix = numpy.array([ [ 1 + 0j, 0j ], [ 0j, -1 + 0j ] ])
```

Secondly: the operator. We will initate an ``Operator`` object and we will pass ``spinMatrix`` as an argument:

```python
S = dirac.Operator(spinMatrix)
```

Next we have to apply the operator to the state:

```python
measuredSpin = S @ psi
```

> **Tip**: The ``act`` method is equivalent to the ``@`` operator:
> ```python
> measuredSpin = S.act(psi)
> ```

When we print ``measuredSpin`` we get:

```console
[
        spin-up: 0.7071067811865476 + 0.0i 
        spin-down: 0.0 + -0.7071067811865476i 
]
```

... hbar, change of basis ...

### **The Wave Function**

So far we have only used quantized states. However in real life we observe **continuous** basis. Suppose we have a particle in free space. It is in a superposition of possible  positions. But space is not quantized. It is **continuous**. We have infinitely many basis states. What could we do?

Mathematically we have a tool called the wave function: $\psi(x)$. This functions returns the probability amplitude of the particle being in position $x$. And it is related to the quantum state like this:

$$ \ket\psi = \int_{-\infty}^\infty dx \: \psi(x) \: \ket{x} $$

This expression is similar to the old definition of quantum state because integration is a continuous sum. Can we bypass the continuum? 

We can approximate the space continuum with finite points with small positional difference. This is called **discretization**. Computers always use this method to do advanced calculations.

To create a discrete basis we will use ``numpy``'s method: ``linspace``:

```python
import numpy

START = -1
END = 1
N = 5

X = numpy.linspace(START, END, N)

print(X)
```

```console
[-1.  -0.5  0.   0.5  1. ]
```

Here ``START`` and ``END`` specify the boundaries of space and ``N`` is the number of points in space. If we want to be more precise we have to use bigger value for ``N``. This costs computational power.

Next we will create an anonymous function. This will be our wave function $\psi(x)$. Let's use $cos(2\pi x)$ for example:

```python
waveFunction = lambda x: numpy.cos(2 * numpy.pi * x)
```

Let's plot the wave function with ``pyplot`` from the ``matplotlib`` library:

```python
Y = waveFunction(X)

pyplot.plot(X, Y)
pyplot.show()
```

<p align="center"><image src="./assets/Figure_1.jpeg" width=70% /></p>

> **Note**: we haven't normalized the probability amplitudes

This doesn's look like a cosine wave. Don't worry. Remember: bigger ``N``: better results. So let's try this with more points. Let's try with ```N = 20```:

<p align="center"><image src="./assets/Figure_2.jpeg" width=70% /></p>

What about ```N = 80```:

<p align="center"><image src="./assets/Figure_3.jpeg" width=70% /></p>

> **Tip**: to see where are the discrete points add ``'o--'`` to ``plot``'s arguments like this:
>
> ```pyhton
> pyplot.plot(X, Y, 'o--')
> ```
> <p align="center"><image src="./assets/Figure_4.jpeg" width=70% /></p>

But there is a catch. What if ``Y`` is not real. After all these are probability amplitudes. They are complex numbers.

The wave function is interpreted as the square root of probability density: $\rho(x)$. We can convert from  probability amplitudes to probability density like this:

$$ \rho(x) = \psi^*(x) \: \psi(x) $$

Probability density is always real. In fact it is always positive. Let's plot $\rho(x)$:

```python
pyplot.plot(X, Y.conjugate() * Y, 'o--')
pyplot.show()
```

<p align="center"><image src="./assets/Figure_5.jpeg" width=70% /></p>

### **The Schrödinger equation**

The core of the **Dirac engine** is the **Dirac equation**:

$$ i \hbar \gamma^\mu \partial_\mu \ket\psi - m c \ket\psi = 0 $$

This equations governs how the quantum state evolves over time. It is the ultimate tool for spin 1/2 particles. However it is not generalized for other particles. Also it works only with **Dirac spinnors**. Can we avoid this?

The answer is yes. Before the **Dirac equation** there was another equation: the **Schrödinger equation**. It does not requires spin nor spinnors. It is not the best description of reality but it is powerful enough to predict the periodic table. Lets's see the **Schrödinger equation**:

$$ i \hbar \frac{d}{dt} \ket\psi = \frac{-\hbar^2}{2m} \nabla^2 \ket\psi + U\ket\psi $$

To solve it, first, we will use code from the previous section:

```python
import diracengine as dirac
import numpy

START = -1
END = 1
N = 80

X = numpy.linspace(START, END, N)

waveFunction = lambda x: numpy.cos(2 * numpy.pi * x)

Y = waveFunction(X)
Y = Y.astype('complex')
```

> **Note**: we used ``astype('complex')`` to ensure that probability amplitudes stay complex. This prevents value exeptions.

Next we will create an instance of the ``WaveFunction`` class. We will use ``Y`` as probability amplitudes and we will set the mass of the particle to 1:

```python
MASS = 1

psi = dirac.WaveFunction(Y, X, mass = MASS)
```

> **Note**: ``WaveFunction`` also normalizes the probability amplitudes by default. You can configure it like ``QuantumState``.

We can plot the wave function's probability density with the ``plot`` method:

```python
psi.plot()
```

<p align="center"><image src="./assets/Figure_6.jpeg" width=70% /></p>

Now let's create a potential field. We will set it to zero. This means that our equation will be:

$$ \frac{d}{dt} \ket\psi = \frac{i \hbar}{2m} \nabla^2 \ket\psi $$

To set the potential field to zero we will map ``X`` to 0:

```python
potential = lambda x: 0
U = potential(X)
```

Now we can solve the equation. Just use the ``shrodingerEvolve`` method. We will pass the amount of time steps. Let's set it to 100 steps:

```python
T = 100

psi.shrodingerEvolve(U, T)
```

To see the results we will use ``animate``:

```python
psi.animate()
```

If everything is OK you should see a animation of the evolution of our initial wave function: $\psi(x) = cos(2\pi x)$. Let's review the code:

```python
import diracengine as dirac
import numpy

START = -1
END = 1
N = 80
T = 100
MASS = 1

waveFunction = lambda x: numpy.cos(2 * numpy.pi * x)
potential = lambda x: 0

X = numpy.linspace(START, END, N)

Y = waveFunction(X)
Y = Y.astype('complex')

psi = WaveFunction(Y, X, mass = MASS)

U = potential(X)

psi.shrodingerEvolve(U, T)
psi.animate()
```

Congratulations! This is your first "Hello Quantum World" program. In the next chapters we will code more advanced scripts. We will see how to do simulations in 2D and 3D. We will simulate the double-slit experiment and the hydrogen atom.