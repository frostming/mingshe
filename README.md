# MíngShé

A better [Python](https://www.python.org/) superset language.

> “鲜山多金玉，无草木，鲜水出焉，而北流注于伊水。其中多鸣蛇，其状如蛇而四翼，其音如磬，见则其邑大旱”——《山海经》

## Install

```
pip install mingshe
```

## Usage

```bash
mingshe --help
```

## Pipe

Example:

```
range(10) |> sum |> print
```

Compile to:

```python
print(sum(range(10)))
```

## Conditional

Example:

```
a ? b : c
```

Compile to:

```python
b if a else c
```

## Partial

Example:

```
square = pow(?, 2)
```

Compile to:

```python
(lambda pow: lambda _0, /: pow(_0, 2))(pow)
```
