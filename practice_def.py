### 関数定義と利用のテスト

## 引数がスコープ内外で関係なく共通の参照渡し
# 関数
def array_operation(arg, result = []):
    result.append(arg)
    print(result)

# ステートメント
arr = ['a', 'b']
array_operation('c', arr) # ['a', 'b', 'c']
array_operation('d') # ['d']
array_operation('e') # ['d', 'e']