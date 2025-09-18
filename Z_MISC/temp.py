CopySource = '/exigent-test-lambda-trigger/Level1/Level2/UHG/New-Text-Document00:00:00.txt'

txt = "apple, banana, cherry"

x = CopySource.rsplit("/")

list_len = len(x)

filename = x[list_len - 1]

print(x)
print(list_len)
print(filename)