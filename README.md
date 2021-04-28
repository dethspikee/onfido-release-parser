# Common uses

1. See all releases for Web SDK
```python
python3 rparser.py | grep Release:
```
2. See release notes for version X.X.X
```python
python3 rparser.py | grep X.X.X -A 20
```
3. See LTS releases for Web SDK
```python
python3 rparser.py | grep 'Release.*LTS'
```
4. Search for keyword in Web SDK release notes
```python
python3 rparser.py | grep <keyword>
```
5. Search for keyword in Web SDK release notes (show 10 lines before and
   after match)
```python
python3 rparser.py | grep <keyword> -A 10 -B 10
```
### rparser can be used as a executable
1. Correct shebang if needed
2. Assert execetuble permissions are granted
3. (optional) Place rparser in your PATH

Same commands apply:

See release notes for version X.X.X
```bash
rparser | grep X.X.X -A 20
```
