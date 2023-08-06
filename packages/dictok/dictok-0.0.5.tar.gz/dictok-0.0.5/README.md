# DicTok

A dictionary-based tokenizer.
It tokenizes a text based on known tokens.

## Installation

```
pip install dictok
```

## Usage

1. Create your dic-file with a list of tokens e.g. `tokens.dic`:

```
super
man
note
book
store
...
```

2. Import `dictok` and pass it the dictionary file as main parameter:

```
>>> import dictok
>>> dt = dictok.DicTok('tokens.dic')
```

3. You are ready to use it:

```
>>> sent = "Superman bought a notebook in the bookstore."
>>> dt.tokenize(sent)
['Super', 'man', 'bought', 'a', 'note', 'book', 'in', 'the', 'book', 'store', '.']
```

## Options

You can also ignore single characters or unknown tokens:

```
>>> dt.tokenize(sent, include_unknown = False, include_single_chars = False)
['Super', 'man', 'note', 'book', 'book', 'store']
```

If you want to rewrite words or, for example, recognize and correct words with typing errors,
you can do so by specifying them as pair in the dictionary:

```
super
man
bought,buy
note
book
buok,book
store
stohre,store
...
```

```
>>> dt = dictok.DicTok('tokens.dic')
>>> sent = "Superman bought a notebuok in the bookstohre."
>>> dt.tokenize(sent, include_unknown = False, include_single_chars = False)
['Super', 'man', 'buy', 'note', 'book', 'book', 'store']
```
