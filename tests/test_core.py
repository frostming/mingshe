import ast
import inspect

import pytest

import mingshe.core


@pytest.mark.parametrize(
    "raw,result",
    [
        # 管道运算符
        (
            "1 |> print",
            "print(1)",
        ),
        (
            "[1] |> max",
            "max([1])",
        ),
        (
            "{1} |> max",
            "max({1})",
        ),
        (
            "{'a': 1} |> max",
            "max({'a': 1})",
        ),
        (
            "range(10) |> sum |> print",
            "print(sum(range(10)))",
        ),
        (
            """
            "hello" |> print
            "world" |> print
            """,
            """
            print("hello")
            print("world")
            """,
        ),
        (
            "10 |> partial(print, 'num:')",
            "partial(print, 'num:')(10)",
        ),
        # 三元运算符
        (
            "a ? b : c",
            "b if a else c",
        ),
        (
            "a ? (b ? d : e) : c",
            "(d if b else e) if a else c",
        ),
        # 偏函数
        (
            "f(?)",
            "(lambda f: (lambda _0, /: f(_0)))(f)",
        ),
        (
            "pow(?, 2)",
            "(lambda pow: lambda _0, /: pow(_0, 2))(pow)",
        ),
        (
            "f(a, b=?)",
            "(lambda _p_0, /, f: lambda _0, /: f(_p_0, b=_0))(a, f)",
        ),
        (
            "f(?, b=0)",
            "(lambda f: lambda _0, /: f(_0, b=0))(f)",
        ),
        (
            "f(1, *?)",
            "(lambda f: lambda _0, /: f(1, *_0))(f)",
        ),
        (
            "f(a, **?)",
            "(lambda _p_0, /, f: lambda _0, /: f(_p_0, **_0))(a, f)",
        ),
        (
            "f(a, *?, **?)",
            "(lambda _p_0, /, f: lambda _0, _1, /: f(_p_0, *_0, **_1))(a, f)",
        )
    ],
)
def test_right_example(raw, result):
    assert ast.dump(mingshe.core.compile(inspect.cleandoc(raw))) == ast.dump(
        ast.parse(inspect.cleandoc(result))
    )


@pytest.mark.parametrize(
    "string",
    [
        "1 |> ",
        "a ? b",
    ]
)
def test_wrong_example(string):
    with pytest.raises(SyntaxError):
        mingshe.core.compile(string)
