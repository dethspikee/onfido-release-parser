# Common uses

1. See LTS releases for Web SDK
```python
python3 release_parser.py | grep 'Release.*LTS'
```
2. Search for keyword in Web SDK release notes
```python
python3 release_parser.py | grep <keyword>
```
3. Search for keyword in Web SDK release notes (show 10 lines before and
   after match)
```python
python3 release_parser.py | grep <keyword> -A 10 -B 10
```
