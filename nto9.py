data = open('data.txt').read()
predictions = open('predictions.txt').read()
tp = 0
fn = 0
print(len(data), len(predictions))
for i in range(len(data)):
    print(type(data[i]))
    if data[i] == '1' and predictions[i] == '1':
        tp += 1
    if data[i] == '1' and predictions[i] == '0':
        fn += 1
print(tp/(tp+fn))
        
