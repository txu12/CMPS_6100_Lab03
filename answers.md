# CMPS 6100 Lab 03
## Answers

**Name:**__________Tiancheng.Xu__________


Place all written answers from `lab-03.md` here.

## Asymptotic Analysis Problems (1 pt. ea.)

1. $32n \in O(n)\\$
Proof:
$\\\lim_{n\to\infty} \frac{32n}{n} =32 $
$\\\therefore 32n \in \Theta(n)$


2. $\ln n \in \Omega(n)\\$
Proof:
$\\\lim_{n\to\infty}\frac{\ln(n)}{n}\\= \lim_{n\to\infty}\frac{\frac{1}{x}}{1}\\=\lim_{n\to\infty}\frac{1}{x}
\\=0$
$\\\therefore \ln(n) \in O(n)$


3. $\lg n \in \Theta(\ln n)\\$
Proof:
$\\\lim_{n\to\infty}\frac{\lg(n)}{\ln(n)}\\=\lim_{n\to\infty}\frac{\frac{1}{x\ln(2)}}{\frac{1}{x}}\\=\frac{1}{\ln(2)}$
$\\\therefore \lg(x)\in\Theta(\ln(n))$


4. $\log_c n \in \Theta(\ln n)$, $~~c > 1\\$
Proof:
$\\\lim_{n\to\infty}\frac{\log_c (n)}{\ln(n)}\\=\frac{1}{\ln(c)}\\$
If c is small, then $\log_c(n)\in \Theta(\ln(n))\\$
If c is large enough, then $\log_c(n)\in O(\ln(n))\\$ 

5. $n^2 \in O(2^n)\\$
Proof:
$\\\lim_{n\to\infty}\frac{n^2}{2^n}\\=\lim_{n\to\infty}\frac{2n}{n2^{n-1}}\\=\lim_{n\to\infty}\frac{2}{n(n-1)2^{n-2}}\\=0\\$
$\therefore n^2\in O（2^n）$



6. $n^3 \in \Omega(n^2)\\$
Proof:
$\\\lim_{n\to\infty}\frac{n^3}{n^2}\\=\lim_{n\to\infty}n\\=\infty\\$
$\therefore n^3\in\Omega(n^2)$



7. $4^{\lg n} \in \Theta(n)\\$
Proof:
$\\\lim_{n\to\infty}\frac{4^{\lg(n)}}{n}\\=\lim_{n\to\infty}\frac{n^2}{n}\\=\lim_{n\to\infty}n\\=\infty\\$
$\therefore 4^{\lg(n)}\in\Omega(n)$



8. $\ln^2 n \in O(n)\\$
Proof:
$\\\lim_{n\to\infty}\frac{\ln^2(n)}{n}\\=\lim_{n\to\infty}\frac{\frac{2\ln(n)}{n}}{1}\\=\lim_{n\to\infty}\frac{2\ln(n)}{n}\\=\lim_{n\to\infty}\frac{2}{n}\\=0\\$
$\therefore \ln^2(n)\in O(n)$



9. $\ln^2 n \in O(\sqrt n)\\$
Proof:
$\\\lim_{n\to\infty}\frac{\ln^2(n)}{\sqrt n}\\=\lim_{n\to\infty}\frac{\frac{2\ln(n)}{n}}{\frac{1}{2\sqrt n}}\\=\lim_{n\to\infty}\frac{4\ln(n)}{\sqrt n}\\=\lim_{n\to\infty}\frac{\frac{4}{n}}{\frac{1}{2\sqrt n}}\\=\lim_{n\to\infty}\frac{8}{\sqrt n}\\=0\\$
$\therefore \ln^2(n)\in O(\sqrt n)$


10. $\ln^c n \in O(n^k)$, $~~\forall ~ c,k > 0\\$ 
Proof:
$\\\lim_{n\to\infty}\frac{\ln^c(n)}{n^k}\\=0\\$
This is similar to question 9, we just need to apply L'Hopital's rule c times.
$\\\therefore \ln^c(n)\in O(n^k),\forall ~ c,k > 0$


11. $\ln \ln n \in O(\ln n)\\$
Proof:
$\\\lim_{n\to\infty}\frac{\ln\ln(n)}{\ln(n)}\\=\lim_{n\to\infty}\frac{\frac{1}{n\ln(n)}}{\frac{1}{n}}\\=\lim_{n\to\infty}\frac{1}{\ln(x)}\\=0\\$
$\therefore \ln\ln(n)\in O(\ln(n))$


12.  $2^n \in \Omega(2^{n+1})\\$
Proof:
$\\\lim_{n\to\infty}\frac{2^n}{2^{n+1}}\\=\frac{1}{2}\\$
$\\\therefore 2^n \in \Theta(2^{n+1})$


## The Ghost Game

Detail any and additional features that you added to the game here. 

13. Detail the attack options for your player.

Player have 100 HP

Player have 3 attack options:

1.Laser gun: deal 10 dmg to ghost.

2.Blast grenade: deal 25 dmg to ghost, but deal 5 dmg to the player himself. 

3.reckless blade: deal 35 dmg to ghost, but has 50% probability to miss.

For attack 2, this will deal damage to the ghost first.

14. If implemented, detail the ghost attack options and game logic for 
ghost attack selection.

Ghost have 100 HP

Ghost have 2 options:

1.Horror claw: deal 15 dmg to player. 

2.blood bite: deal 10 dmg to player, also restore 10 HP if ghost's HP is below 50.

Ghost will randomly perform a kind of attack.
