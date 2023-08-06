def base():
    """
    Help on package torch.nn in torch:

NAME
    torch.nn

PACKAGE CONTENTS
    _reduction
    backends (package)
    common_types
    cpp
    functional
    grad
    init
    intrinsic (package)
    modules (package)
    parallel (package)
    parameter
    qat (package)
    quantizable (package)
    quantized (package)
    utils (package)

FUNCTIONS
    factory_kwargs(kwargs)
        Given kwargs, returns a canonicalized dict of factory kwargs that can be directly passed
        to factory functions like torch.empty, or errors if unrecognized kwargs are present.

        This function makes it simple to write code like this::

            class MyModule(nn.Module):
                def __init__(self, **kwargs):
                    factory_kwargs = torch.nn.factory_kwargs(kwargs)
                    self.weight = Parameter(torch.empty(10, **factory_kwargs))

        Why should you use this function instead of just passing `kwargs` along directly?

        1. This function does error validation, so if there are unexpected kwargs we will
        immediately report an error, instead of deferring it to the factory call
        2. This function supports a special `factory_kwargs` argument, which can be used to
        explicitly specify a kwarg to be used for factory functions, in the event one of the
        factory kwargs conflicts with an already existing argument in the signature (e.g.
        in the signature ``def f(dtype, **kwargs)``, you can specify ``dtype`` for factory
        functions, as distinct from the dtype argument, by saying
        ``f(dtype1, factory_kwargs={"dtype": dtype2})``)

FILE
    \envsgang xinghuo\lib\site-packages\torchn\__init__.py

    a = [[1, 2, 3], [4, 5, 6]]
    a_tensor = torch.tensor(a)

    a_tensor.size()
    a_tensor.numel()
    a_tensor.tolist()
    b = np.array([[0, 0], [1, 1]])
    b_tensor = torch.from_numpy(b)
    b_tensor.numpy()
    rand_tensor = torch.rand(shape)
    ones_tensor = torch.ones(shape)
    zeros_tensor = torch.zeros(shape)

    if torch.cuda.is_available():
    zeros_tensor = zeros_tensor.to('cuda')
    a_tensor = torch.arange(0, 6)
    a_tensor.view(2, 3)
    c_tensor = torch.rand(4, 4)
    d_tensor = torch.rand(3,2)
    e_tensor = torch.add(d_tensor, 10)
    c = torch.div(a, b)
    a = torch.randint(10, (3, 4))
    b = torch.pow(a, 2)
    torch.argmax(a, dim=1)
    b = torch.cumprod(a, dim=1)
    b = torch.unsqueeze(a, 1)
    c=torch.squeeze(b, 1)

    torch.manual_seed(1000)

    def fake_data(batch_size=10):
       x = torch.rand(batch_size, 1) * 20
       y = x * 2 + (1 + torch.rand(batch_size, 1)) * 3
       return x, y

    x, y = fake_data()
    w = torch.rand(1, 1)
    b = torch.zeros(1, 1)

    lr = 0.001

    for index in range(10000):
    x, y = fake_data()

    y_pred = x.mm(w) + b.expand_as(y)

    loss = 0.5 * (y_pred - y) ** 2
    loss = loss.sum()

    dloss = 1
    dy_pred = dloss * (y_pred - y)

    dw = x.t().mm(dy_pred)
    db = dy_pred.sum()

    w.sub_(lr * dw)
    b.sub_(lr * db)

    if index % 1000 == 0:
        display.clear_output(wait=True)

        x = torch.arange(0, 20).view(-1, 1)
        y = x * w + b.expand_as(x)
        plt.plot(x.numpy(), y.numpy())

        x2, y2 = fake_data(batch_size=20)
        plt.scatter(x2.numpy(), y2.numpy())

        plt.xlim(0, 20)
        plt.ylim(0, 41)
        plt.show()
        # Loss的变化以及学习到的参数
        print('Loss: ', loss.squeeze().numpy())
        print('W: ', w.squeeze().numpy())
        print('b: ', b.squeeze().numpy())
        plt.pause(2)

        a = torch.ones(3, 4, requires_grad=True)
        b = torch.zeros(3, 4)
        c = a.add(b)

        a.requires_grad, b.requires_grad, c.requires_grad

        x = torch.rand(1)
        b = torch.rand(1, requires_grad=True)
        w = torch.rand(1, requires_grad=True)
        y = w * x
        z = y + b
        x.is_leaf, b.is_leaf, w.is_leaf, y.is_leaf, z.is_leaf

        y.grad_fn.next_functions
        z.backward()
        b.grad

        torch.manual_seed(1000)

        def fake_data(batch_size=10):
            x = torch.rand(batch_size, 1) * 20
            y = x * 2 + (1 + torch.rand(batch_size, 1)) * 3
            return x, y

        x, y = fake_data()

        w = torch.rand(1, 1, requires_grad=True)
        b = torch.zeros(1, 1, requires_grad=True)

        lr = 0.001

        for index in range(10000):
    x, y = fake_data()

    # 进行前向计算，得到预测值
    y_pred = x.mm(w) + b.expand_as(y)
    # 均方误差作为loss
    loss = 0.5 * (y_pred - y) ** 2
    loss = loss.sum()

    # loss进行反向传播
    loss.backward()

    # 无需手动计算梯度，直接使用梯度进行参数更新
    w.data.sub_(lr * w.grad.data)
    b.data.sub_(lr * b.grad.data)

    # 更新后，梯度清零
    w.grad.data.zero_()
    b.grad.data.zero_()

    # 可视化更新过程
    if index % 1000 == 0:
        display.clear_output(wait=True)

        x = torch.arange(0, 20).view(-1, 1)
        y = x * w + b.expand_as(x)
        plt.plot(x.detach().numpy(), y.detach().numpy())

        x2, y2 = fake_data(batch_size=20)
        plt.scatter(x2.numpy(), y2.numpy())

        plt.xlim(0, 20)
        plt.ylim(0, 41)
        plt.show()
        # Loss的变化以及学习到的参数
        print('Loss: ', loss.detach().squeeze().numpy())
        print('W: ', w.detach().squeeze().numpy())
        print('b: ', b.detach().squeeze().numpy())

        plt.pause(2)

        features = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
        label = 'MDEV'

        X = df.drop(['MDEV', 'RAD'], axis = 1)
        y = df['MDEV']

        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import MinMaxScaler

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

        scaler = MinMaxScaler()
        scaler.fit(X_train)

        X_train = scaler.transform(X_train)
        X_test = scaler.transform(X_test)

        inputs = torch.unsqueeze(torch.FloatTensor(X_train.astype(np.float32)), dim=1)  #torch.Size([354, 1, 12])
        targets = torch.unsqueeze(torch.FloatTensor(y_train.astype(np.float32)), dim=1).reshape(-1, 1, 1)
        dataset = torch.utils.data.TensorDataset(inputs, targets)
        loader = torch.utils.data.DataLoader(dataset, batch_size=64, shuffle=True)

        class LinearRegression(nn.Module):
    def __init__(self, input_size, output_size):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(input_size, output_size)

    def forward(self, x):
        out = self.linear(x)
        return out

        model = LinearRegression(input_size=12, output_size=1)

    summary(model, input_size=(1, 12), device='cpu')

    criterion = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-2)

    num_epochs = 1000

    for epoch in range(num_epochs):

        for inps, tars in loader:
            outputs = model(inps)
            optimizer.zero_grad()
            loss = criterion(outputs, tars)
            loss.backward()
            optimizer.step()

        if (epoch + 1) % 100 == 0:
            print(f"Epoch {epoch + 1} / {num_epochs}, Loss: {loss.detach().numpy()}")

    model.eval()
    test_inputs = torch.unsqueeze(torch.FloatTensor(X_test.astype(np.float32)), dim=1)
    test_pred = model(test_inputs)
    test_pred = test_pred.data.squeeze().numpy()

    mse = metrics.mean_squared_error(y_test, test_pred)
    print("MSE = ", mse)

    print("Model's state_dict:")
    for param_tensor in model.state_dict():
        print(param_tensor, "\t", model.state_dict()[param_tensor].numpy()[0])
        """
        
    return ""

def textv1():
    '''
    Help on package torch.nn in torch:

NAME
    torch.nn

PACKAGE CONTENTS
    _reduction
    backends (package)
    common_types
    cpp
    functional
    grad
    init
    intrinsic (package)
    modules (package)
    parallel (package)
    parameter
    qat (package)
    quantizable (package)
    quantized (package)
    utils (package)

FUNCTIONS
    factory_kwargs(kwargs)
        Given kwargs, returns a canonicalized dict of factory kwargs that can be directly passed
        to factory functions like torch.empty, or errors if unrecognized kwargs are present.

        This function makes it simple to write code like this::

            class MyModule(nn.Module):
                def __init__(self, **kwargs):
                    factory_kwargs = torch.nn.factory_kwargs(kwargs)
                    self.weight = Parameter(torch.empty(10, **factory_kwargs))

        Why should you use this function instead of just passing `kwargs` along directly?

        1. This function does error validation, so if there are unexpected kwargs we will
        immediately report an error, instead of deferring it to the factory call
        2. This function supports a special `factory_kwargs` argument, which can be used to
        explicitly specify a kwarg to be used for factory functions, in the event one of the
        factory kwargs conflicts with an already existing argument in the signature (e.g.
        in the signature ``def f(dtype, **kwargs)``, you can specify ``dtype`` for factory
        functions, as distinct from the dtype argument, by saying
        ``f(dtype1, factory_kwargs={"dtype": dtype2})``)

FILE
    \envsgang xinghuo\lib\site-packages\torchn\__init__.py

    with open('./dataset/baidu_stopwords.txt', 'r') as f:
        stop_words = f.read().split('')

    def cut_and_clean(text):
        cuted_text = ' '.join([x for x in jieba.lcut(text) if x not in stop_words and len(x) > 1])
        clean_text = re.sub('([\.，。、“”‘ ’？\?:#：【】\+!！])', ' ', cuted_text)
        clean_text = re.sub('\s{2,}', ' ', clean_text)
        return clean_text

    cut_and_clean(text)
    import wordcloud
    WC = wordcloud.WordCloud(font_path='./dataset/MSYH.TTC',
                         max_words=1000,
                         height= 600,
                         width=1200,
                         background_color='white',
                         repeat=False,
                         mode='RGBA')
    word_cloud_img = WC.generate(train_text)
    plt.figure(figsize = (20,10))
    plt.imshow(word_cloud_img, interpolation='nearest')
    plt.axis("off")
    WC.to_file('./dataset/wordcloud.png')

    def preprocess_text(text):
    text = text.lower()
    text = ' '.join([x for x in jieba.lcut(text) if x])
    text = re.sub('[^a-z^0-9^gang u4e00-gang u9fa5]', ' ', text)
    text = re.sub('[0-9]', '0', text)
    text = re.sub('\s{2,}', ' ', text)
    return text.strip()

    unlabeled_df['processed_text'] = unlabeled_df['text'].apply(preprocess_text)
    total_sentences = unlabeled_df['processed_text']

    from gensim.models.word2vec import Word2Vec

    model = Word2Vec(sentences,       # 语料集
                 sg=1,            # 使用skip-gram算法
                 vector_size=30,  # 词向量长度
                 window=5,       # 上下问窗口大小
                 min_count=10,  # 词最少出现的次数
                 workers=4,    # 训练的并行数，这里为4核
                 epochs=3      # 迭代次数，这里做演示只设置了3次
                )

    for word in ['肺炎', '武汉', '钟南山', '加油', '感人']:
        result = model.wv.most_similar(word, topn=10)
        print(word)
        print(result)

        embedding_path = './dataset/sg_ns_30.txt'

    model.wv.save_word2vec_format(embedding_path,binary=False)

    vocab_file = 'dataset/sg_ns_30.txt'

    word_2_id = {'<PAD>': 0, '<UNK>': 1}
    id_2_word = {0: '<PAD>', 1: '<UNK>'}
    vectors = [np.zeros((30,)), np.zeros((30,))]

    with open(vocab_file, 'r' ,encoding='utf-8') as f:
    for index, line in enumerate(f.readlines()):
        if index == 0:
            continue
        items = line.split(' ')
        word = items[0]
        vec = np.array([float(x) for x in items[1:]])
        vectors.append(vec)
        word_2_id[word] = index + 1
        id_2_word[index + 1] = word

MAX_SEQ_LEN = 200

with open('./dataset/baidu_stopwords.txt', 'r',encoding='utf-8') as f:
    stop_words = f.read().split('')

def sentence_2_id(sentence):
    return [word_2_id.get(w, 1) for w in sentence]

def tokenizer(text):
    text = ' '.join([x for x in jieba.lcut(text) if x and x not in stop_words])
    text = re.sub('[^a-z^0-9^gang u4e00-gang u9fa5]', ' ', text)     # 去除标点，这里只训练中英文字符
    text = re.sub('[0-9]', '0', text)                        # 将所有数字都转为0
    text = re.sub('\s{2,}', ' ', text)                       #合并连续的空格
    sentence = text.strip().split(' ')
    ids = sentence_2_id(sentence)
    ids = ids[:MAX_SEQ_LEN]
    if len(ids) < MAX_SEQ_LEN:
        ids.extend([0] * (MAX_SEQ_LEN - len(ids)))
    ids_tensor = torch.LongTensor(ids)
    return ids_tensor

    VOCAB_SIZE = len(word_2_id)

BATCH_SIZE = 32
class Dataset(torch.utils.data.Dataset):

    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.labels = self.df['label'].values
        self.texts = [tokenizer(text) for text in self.df['text']]

    def classes(self):
        return self.labels

    def __len__(self):
        return len(self.labels)

    def get_batch_labels(self, idx):
        # Fetch a batch of labels
        return np.array(self.labels[idx])

    def get_batch_texts(self, idx):
        # Fetch a batch of inputs
        return self.texts[idx]

    def __getitem__(self, idx):

        batch_texts = self.get_batch_texts(idx)
        batch_y = self.get_batch_labels(idx)
        return batch_texts, batch_y

    train, val, test = Dataset(train_df), Dataset(val_df), Dataset(test_df)

    train_dataloader = torch.utils.data.DataLoader(train, batch_size=BATCH_SIZE, shuffle=True)
    val_dataloader = torch.utils.data.DataLoader(val, batch_size=BATCH_SIZE)
    test_dataloader = torch.utils.data.DataLoader(test, batch_size=BATCH_SIZE)

    import torch
from torch import nn
import torch.nn.functional as F

class TextCNN(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_filters, filter_sizes, num_classes, dropout):
        super(TextCNN, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)

        self.convs = nn.ModuleList([nn.Conv2d(1, num_filters, (k, embed_dim)) for k in filter_sizes])

        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(num_filters * len(filter_sizes), num_classes)

    def conv_and_pool(self, x, conv):
        x = F.relu(conv(x)).squeeze(3)
        x = F.max_pool1d(x, x.size(2)).squeeze(2)
        return x

    def forward(self, x):
        out = self.embedding(x)
        out = out.unsqueeze(1)
        out = torch.cat([self.conv_and_pool(out, conv) for conv in self.convs], 1)
        out = self.dropout(out)
        out = self.fc(out)
        return out

    num_class = 3
    num_filters = 128
    filter_sizes = [2, 3, 4]
    emsize = 30
    dropout = 0.5
    model = TextCNN(VOCAB_SIZE, emsize, num_filters, filter_sizes, num_class, dropout)

    model.embedding.weight.data.copy_(torch.Tensor(vectors))
    model.to(device)

    EPOCHS = 10 # epoch
LR = 3e-4  # learning rate

criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=LR)

for epoch in range(1, EPOCHS + 1):
    model.train()
    total_acc, total_count = 0, 0

    idx = 0
    for train_input, label in train_dataloader:

        predicted_label = model(train_input.to(device))
        label = label.to(device)

        optimizer.zero_grad() #
        loss = criterion(predicted_label, label)

        loss.backward()
        optimizer.step()

        total_acc += (predicted_label.argmax(1) == label).sum().item()
        total_count += label.size(0)

        if (idx + 1) % 10 == 0:
            print('| epoch {:3d} | {:5d}/{:5d} batches '
                  '| accuracy {:8.3f}'.format(epoch, idx, len(train_dataloader), total_acc / total_count))
        idx += 1
    print('-' * 60)
    val_result = evaluate(model, val_dataloader)
    print(val_result)
    print('-' * 60)

    test_result = evaluate(model, test_dataloader)
    '''

def textv2():
    '''
    Help on package torch.nn in torch:

NAME
    torch.nn

PACKAGE CONTENTS
    _reduction
    backends (package)
    common_types
    cpp
    functional
    grad
    init
    intrinsic (package)
    modules (package)
    parallel (package)
    parameter
    qat (package)
    quantizable (package)
    quantized (package)
    utils (package)

FUNCTIONS
    factory_kwargs(kwargs)
        Given kwargs, returns a canonicalized dict of factory kwargs that can be directly passed
        to factory functions like torch.empty, or errors if unrecognized kwargs are present.

        This function makes it simple to write code like this::

            class MyModule(nn.Module):
                def __init__(self, **kwargs):
                    factory_kwargs = torch.nn.factory_kwargs(kwargs)
                    self.weight = Parameter(torch.empty(10, **factory_kwargs))

        Why should you use this function instead of just passing `kwargs` along directly?

        1. This function does error validation, so if there are unexpected kwargs we will
        immediately report an error, instead of deferring it to the factory call
        2. This function supports a special `factory_kwargs` argument, which can be used to
        explicitly specify a kwarg to be used for factory functions, in the event one of the
        factory kwargs conflicts with an already existing argument in the signature (e.g.
        in the signature ``def f(dtype, **kwargs)``, you can specify ``dtype`` for factory
        functions, as distinct from the dtype argument, by saying
        ``f(dtype1, factory_kwargs={"dtype": dtype2})``)

FILE
    c:gang users\ \anaconda3\envsgang xinghuo\lib\site-packages\torchn\__init__.py

    import torch
from torchtext.legacy import data, datasets
from torchtext.vocab import Vectors
from sklearn.metrics import classification_report

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

import re
import jieba

with open('./dataset/baidu_stopwords.txt', 'r', encoding="UTF-8") as f:
    stop_words = f.read().split('')

def tokenizer(text):
    text = ' '.join([x for x in jieba.lcut(text) if x])
    text = re.sub('[^a-z^0-9^gang u4e00-gang u9fa5]', ' ', text)
    text = re.sub('[0-9]', '0', text)
    text = re.sub('\s{2,}', ' ', text)
    return text.strip().split(' ')

LABEL = data.Field(sequential=False, use_vocab=False)
TEXT = data.Field(sequential=True, tokenize=tokenizer, stop_words=stop_words, fix_length=200,
                  batch_first=True, lower=True)

train = data.TabularDataset('./dataset/train.csv', format='csv',skip_header=True,
        fields=[('text', TEXT), ('label', LABEL)])
val = data.TabularDataset('./dataset/val.csv', format='csv',skip_header=True,
        fields=[('text', TEXT), ('label', LABEL)])
test = data.TabularDataset('./dataset/test.csv', format='csv',skip_header=True,
        fields=[('text', TEXT), ('label', LABEL)])

sample = val[0]
print(sample)
print(sample.__dict__.keys())
print(sample.text, sample.label)

import torchtext.vocab as vocab
vectors = vocab.Vectors('./dataset/sg_ns_30.txt','./cache')
vectors.get_vecs_by_tokens('浙江')

vectors.vectors.shape

TEXT.build_vocab(train, vectors=vectors)

print(TEXT.vocab.itos[100])
print(TEXT.vocab.stoi['浙江'])

词向量矩阵: TEXT.vocab.vectors
print(TEXT.vocab.vectors.shape)
word_vec = TEXT.vocab.vectors[TEXT.vocab.stoi['浙江']]
print(word_vec.shape)
print(word_vec)

BATCH_SIZE = 32 # batch size for training

train_iter = data.BucketIterator(train, batch_size=BATCH_SIZE, sort_key=lambda x: len(x.text),
                                 shuffle=True, device=device)

val_iter = data.Iterator(dataset=val, batch_size=BATCH_SIZE, train=False,
                          sort=False, device=device)

test_iter = data.Iterator(dataset=test, batch_size=BATCH_SIZE, train=False,
                          sort=False, device=device)

    from torch import nn
import torch.nn.functional as F

class TextCNN(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_filters, filter_sizes, num_classes, dropout):
        super(TextCNN, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)

        self.convs = nn.ModuleList([nn.Conv2d(1, num_filters, (k, embed_dim)) for k in filter_sizes])

        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(num_filters * len(filter_sizes), num_classes)

    def conv_and_pool(self, x, conv):
        x = F.relu(conv(x)).squeeze(3)
        x = F.max_pool1d(x, x.size(2)).squeeze(2)
        return x

    def forward(self, x):
        out = self.embedding(x.type(torch.LongTensor))
        out = out.unsqueeze(1)
        out = torch.cat([self.conv_and_pool(out, conv) for conv in self.convs], 1)
        out = self.dropout(out)
        out = self.fc(out)
        return out

num_class = 3
vocab_size = len(TEXT.vocab)
num_filters = 128
filter_sizes = [2, 3, 4]
emsize = 30
dropout = 0.5
model = TextCNN(vocab_size, emsize, num_filters, filter_sizes, num_class, dropout)
# 加载预训练的词向量
model.embedding.weight.data.copy_(TEXT.vocab.vectors)
model.to(device)

def evaluate(model, dataloader):
    model.eval()
    val_preds, val_trues = [], []
    with torch.no_grad():
        for idx, batch in enumerate(dataloader):
            text, label = batch.text, batch.label
            predicted_label = model(text)
            val_preds.extend(predicted_label.argmax(1).cpu().numpy())
            val_trues.extend(label.cpu().numpy())
    result = classification_report(val_trues, val_preds)
    return result

EPOCHS = 10 # epoch
LR = 3e-4  # learning rate

criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=LR)

for epoch in range(1, EPOCHS + 1):
    model.train()
    total_acc, total_count = 0, 0
    for idx, batch in enumerate(train_iter):
        text, label = batch.text, batch.label

        optimizer.zero_grad()
        predicted_label = model(text)
        one_hot_label = torch.nn.functional.one_hot(label, 3).type(torch.FloatTensor).to(device)
        loss = criterion(predicted_label, one_hot_label)

        loss.backward()
        optimizer.step()

        total_acc += (predicted_label.argmax(1) == label).sum().item()
        total_count += label.size(0)

        if (idx + 1) % 10 == 0:
            print('| epoch {:3d} | {:5d}/{:5d} batches '
                  '| accuracy {:8.3f}'.format(epoch, idx, len(train_iter), total_acc/total_count))

    # 查看验证集分类结果
    print('-' * 60)
    val_result = evaluate(model, val_iter)
    print(val_result)
    print('-' * 60)

test_result = evaluate(model, test_iter)

    '''
    return ""
def image():
    '''
    Help on package torch.nn in torch:

NAME
    torch.nn

PACKAGE CONTENTS
    _reduction
    backends (package)
    common_types
    cpp
    functional
    grad
    init
    intrinsic (package)
    modules (package)
    parallel (package)
    parameter
    qat (package)
    quantizable (package)
    quantized (package)
    utils (package)

FUNCTIONS
    factory_kwargs(kwargs)
        Given kwargs, returns a canonicalized dict of factory kwargs that can be directly passed
        to factory functions like torch.empty, or errors if unrecognized kwargs are present.

        This function makes it simple to write code like this::

            class MyModule(nn.Module):
                def __init__(self, **kwargs):
                    factory_kwargs = torch.nn.factory_kwargs(kwargs)
                    self.weight = Parameter(torch.empty(10, **factory_kwargs))

        Why should you use this function instead of just passing `kwargs` along directly?

        1. This function does error validation, so if there are unexpected kwargs we will
        immediately report an error, instead of deferring it to the factory call
        2. This function supports a special `factory_kwargs` argument, which can be used to
        explicitly specify a kwarg to be used for factory functions, in the event one of the
        factory kwargs conflicts with an already existing argument in the signature (e.g.
        in the signature ``def f(dtype, **kwargs)``, you can specify ``dtype`` for factory
        functions, as distinct from the dtype argument, by saying
        ``f(dtype1, factory_kwargs={"dtype": dtype2})``)

FILE
    \envsgang xinghuo\lib\site-packages\torchn\__init__.py

    from PIL import Image
    img_PIL = Image.open(img_path)
    import cv2
    img_cv = cv2.imread(img_path)
    import matplotlib.pyplot as plt
    img_plt = plt.imread(img_path)
    from torchvision.io import read_image
    img_torch = read_image(img_path)

    def show_images(imgs, num_rows, num_cols, titles=None, scale=1.5):
    """Plot a list of images.
    Defined in :numref:`sec_fashion_mnist`"""
    figsize = (num_cols * scale, num_rows * scale)
    _, axes = plt.subplots(num_rows, num_cols, figsize=figsize)
    axes = axes.flatten()
    for i, (ax, img) in enumerate(zip(axes, imgs)):
        if torch.is_tensor(img):
            # 图片张量
            ax.imshow(img.numpy())
        else:
            # PIL图片
            ax.imshow(img)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        if titles:
            ax.set_title(titles[i])
    return axes

def apply(img, aug, num_rows=2, num_cols=4, scale=1.5):   #50%左右的概率翻转
    Y = [aug(img) for _ in range(num_rows * num_cols)]
    show_images(Y, num_rows, num_cols, scale=scale)

    augs = torchvision.transforms.Compose([
    torchvision.transforms.RandomHorizontalFlip(), torchvision.transforms.RandomVerticalFlip(),
    torchvision.transforms.ColorJitter(brightness=0.5, contrast=0.5, saturation=0.5, hue=0.5),
    torchvision.transforms.RandomResizedCrop((200, 200), scale=(0.5, 1), ratio=(0.5, 2))])

    import random
    import torch
    import torch.nn as nn
    import torch.optim as optim
    import numpy as np
    import torchvision
    from torchvision import datasets, transforms
    from torch.utils import data
    import torch.nn.functional as F
    from torchsummary import summary

    import matplotlib.pyplot as plt
    import time
    import os

    ROOT = './data/mnist_data/'
IMG_SIZE = 28
BATCH_SIZE = 32

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

data_transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),  #将图像转换为灰度图像，默认通道数为1
    transforms.Resize((IMG_SIZE, IMG_SIZE)),  #缩放指定宽和高
    transforms.ToTensor(),
#transforms.ToTensor()可将PIL和numpy格式的数据从[0,255]范围转换到[0,1] ，即将原始数据除以255。原始数据的shape是（H W C），shape会变为（C H W）
])

mnist_train = datasets.ImageFolder(root=os.path.join(ROOT, 'train'), transform=data_transform)
mnist_val = datasets.ImageFolder(root=os.path.join(ROOT, 'val'), transform=data_transform)

mnist_train_iter = data.DataLoader(mnist_train, BATCH_SIZE, shuffle=True, num_workers=4)
#dataloader一次性创建num_worker个worker进程，worker将它负责的batch加载进RAM
mnist_val_iter = data.DataLoader(mnist_val, BATCH_SIZE, shuffle=False, num_workers=4)

ROW_IMG = 10
N_ROWS = 5

fig = plt.figure(figsize=(16, 8))
for index in range(1, ROW_IMG * N_ROWS + 1):
    plt.subplot(N_ROWS, ROW_IMG, index)
    plt.axis('off')
    random_num = random.randint(0, len(mnist_train))
    random_x = mnist_train[random_num][0]
    plt.imshow(random_x.squeeze().numpy(), cmap='gray_r')          # squeeze()对数据的维度进行压缩，去掉维数为1的的维度
fig.suptitle('MNIST Dataset - preview')

RANDOM_SEED = 42
LEARNING_RATE = 0.001
N_EPOCHS = 20
N_CLASSES = 10

class LeNet5(nn.Module):

    def __init__(self, n_classes):
        super(LeNet5, self).__init__()

        self.feature_extractor = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5, padding=2),
            nn.Tanh(),
            nn.AvgPool2d(kernel_size=2, stride=2),
            nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5, stride=1),
            nn.Tanh(),
            nn.AvgPool2d(kernel_size=2, stride=2)
        )

        self.classifier = nn.Sequential(
            nn.Linear(in_features=16 * 5 * 5, out_features=120),  #全连接
            nn.Tanh(),
            nn.Linear(in_features=120, out_features=84),
            nn.Tanh(),
            nn.Linear(in_features=84, out_features=n_classes),
        )

    def forward(self, x):  #前向传播
        x = self.feature_extractor(x)
        x = torch.flatten(x, 1)
        logits = self.classifier(x)  #  n_classes*1
        probs = F.softmax(logits, dim=1)  # import torch.nn.functional as F
        return logits, probs

    torch.manual_seed(RANDOM_SEED)
model = LeNet5(N_CLASSES).to(DEVICE)
summary(model, input_size=(1, IMG_SIZE, IMG_SIZE))

optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)
criterion = nn.CrossEntropyLoss()

loss.item()

since = time.time()
train_losses, val_losses = [], []

for epoch in range(N_EPOCHS + 1):
    print('Epoch {}/{}'.format(epoch, N_EPOCHS))
    print('-' * 10)
    model.train()  #设置模型为训练模式，启用 Batch Normalization 和 Dropout

    train_loss, train_corrects = 0.0, 0
    for inputs, labels in mnist_train_iter:
        inputs = inputs.to(DEVICE)
        labels = labels.to(DEVICE)
        # zero the parameter gradients
        optimizer.zero_grad()

        with torch.set_grad_enabled(True):
            logits, probs = model(inputs)
            preds = torch.argmax(probs, 1)
            loss = criterion(logits, labels)#不需要现将输出经过softmax层，否则计算的损失会有误，即直接将网络输出用来计算损失即可
            loss.backward()
            optimizer.step()  #优化器step()方法来对所有的参数进行更新
            #loss.item()应该是一个batch size的平均损失，×inputs.size(0)那就是一个batch size的总损失
            train_loss += loss.item() * inputs.size(0)
            train_corrects += torch.sum(preds == labels.data)

    train_epoch_loss = train_loss / len(mnist_train)
    train_epoch_acc = train_corrects.double() / len(mnist_train)
    print('Train Loss: {:.4f} Acc: {:.4f}'.format(train_epoch_loss, train_epoch_acc))
    train_losses.append(train_epoch_loss)

    # val
    model.eval()   #设置模型为评估模式，不启用 Batch Normalization 和 Dropout
    val_loss, val_corrects = 0.0, 0
    for inputs, labels in mnist_val_iter:
        inputs = inputs.to(DEVICE)
        labels = labels.to(DEVICE)
        # zero the parameter gradients
        optimizer.zero_grad()

        with torch.set_grad_enabled(False):
            logits, probs = model(inputs)
            preds = torch.argmax(probs, 1)
            loss = criterion(logits, labels)
            val_loss += loss.item() * inputs.size(0)
            val_corrects += torch.sum(preds == labels.data)

    val_epoch_loss = val_loss / len(mnist_val)
    val_epoch_acc = val_corrects.double() / len(mnist_val)
    print('Val Loss: {:.4f} Acc: {:.4f}'.format(val_epoch_loss, val_epoch_acc))
    val_losses.append(val_epoch_loss)

time_elapsed = time.time() - since
print('Training complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))

def plot_losses(train_losses, valid_losses):

    # temporarily change the style of the plots to seaborn
    plt.style.use('seaborn')

    train_losses = np.array(train_losses)
    valid_losses = np.array(valid_losses)

    fig, ax = plt.subplots(figsize = (8, 4.5))

    ax.plot(train_losses, color='blue', label='Training loss')
    ax.plot(valid_losses, color='red', label='Validation loss')
    ax.set(title="Loss over epochs",
            xlabel='Epoch',
            ylabel='Loss')
    ax.legend()
    fig.show()

    # change the plot style to default
    plt.style.use('default')

    OW_IMG = 10
N_ROWS = 5

fig = plt.figure(figsize=(16, 8))
for index in range(1, ROW_IMG * N_ROWS + 1):
    plt.subplot(N_ROWS, ROW_IMG, index)
    plt.axis('off')
    random_num = random.randint(0, len(mnist_val))
    random_x = mnist_val[random_num][0]
    random_y = mnist_val[random_num][1]
    plt.imshow(random_x.squeeze().numpy(), cmap='gray_r')

    with torch.no_grad():
        model.eval()
        _, probs = model(random_x.unsqueeze(0).to(DEVICE))

    title = f'[{random_y}: {torch.argmax(probs)} {torch.max(probs * 100):.0f}%]'

    plt.title(title, fontsize=15)
fig.suptitle('LeNet-5 - predictions')

# 对训练数据进行数据增强和规范化
# 对验证数据只需要进行规范化

data_transforms = {
    'train': transforms.Compose([
        torchvision.transforms.RandomVerticalFlip() 使图像各有50%的几率向上或向下翻转
        torchvision.transforms.RandomHorizontalFlip() 使图像各有50%的几率左右翻转图像
        torchvision.transforms.RandomResizedCrop((200, 200), scale=(0.5, 1), ratio=(0.5, 2))
        torchvision.transforms.ColorJitter(brightness=0.5, contrast=0, saturation=0, hue=0)
        transforms.RandomResizedCrop(224,scale=(0.5,1)),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}

data_dir = './data/catsdogs/'
image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x), data_transforms[x])for x in ['train', 'val']}

dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x],
                                              batch_size=4,
                                              shuffle=True,
                                              num_workers=4) for x in ['train', 'val']}

dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'val']}

class_names = image_datasets['train'].classes

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def imshow(inp, title=None):
    """Imshow for Tensor."""
    inp = inp.numpy().transpose((1, 2, 0))
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    inp = std * inp + mean
    inp = np.clip(inp, 0, 1) #将数组中的元素限制在0, 1之间
    plt.imshow(inp)
    if title is not None:
        plt.title(title)
    plt.pause(0.001)  # pause a bit so that plots are updated

# Get a batch of training data
inputs, classes = next(iter(dataloaders['train']))

# Make a grid from batch
out = torchvision.utils.make_grid(inputs)

imshow(out, title=[class_names[x] for x in classes])

def train_model(model, criterion, optimizer, scheduler, num_epochs=25):
    since = time.time()
# copy.copy()是浅拷贝，只拷贝父对象，不会拷贝对象的内部的子对象。
# copy.deepcopy()是深拷贝，会拷贝对象及其子对象，哪怕以后对其有改动，也不会影响其第一次的拷贝。
    best_model_wts = copy.deepcopy(model.state_dict())  # model.state_dict() W,B的参数
    best_acc = 0.0

    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs - 1))
        print('-' * 10)

        # 每个Epoch都进行train, val
        for phase in ['train', 'val']:
            if phase == 'train':
                model.train()   # 设置模型为训练模式
            else:
                model.eval()    # 设置模型为评估模式

            running_loss = 0.0
            running_corrects = 0

            # 在所有数据上迭代.
            for inputs, labels in dataloaders[phase]:
                inputs = inputs.to(device)
                labels = labels.to(device)

                # 参数梯度归零
                optimizer.zero_grad()

                # 前向反馈
                # 训练时追踪指标历史
                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)

                    # 训练时进行反向传播与优化
                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                # 指标统计
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)
            if phase == 'train':
                scheduler.step()

            epoch_loss = running_loss / dataset_sizes[phase]
            epoch_acc = running_corrects.double() / dataset_sizes[phase]

            print('{} Loss: {:.4f} Acc: {:.4f}'.format(
                phase, epoch_loss, epoch_acc))

            # 深拷贝模型
            if phase == 'val' and epoch_acc > best_acc:
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())

        print()

    time_elapsed = time.time() - since
    print('Training complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))
    print('Best val Acc: {:4f}'.format(best_acc))

    # 将最好的模型参数给最终的模型
    model.load_state_dict(best_model_wts)
    return model

    model_ft.state_dict()
    def visualize_model(model, num_images=6):
    was_training = model.training
    model.eval()
    images_so_far = 0
    fig = plt.figure()

    with torch.no_grad():
        for i, (inputs, labels) in enumerate(dataloaders['val']):
            inputs = inputs.to(device)
            labels = labels.to(device)

            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)

            for j in range(inputs.size()[0]):
                images_so_far += 1
                ax = plt.subplot(num_images//2, 2, images_so_far)
                ax.axis('off')
                ax.set_title('predicted: {}'.format(class_names[preds[j]]))
                imshow(inputs.cpu().data[j])

                if images_so_far == num_images:
                    model.train(mode=was_training)
                    return
        model.train(mode=was_training)

        model_ft = models.vgg16(pretrained=True)

        model_ft.classifier[-1]

        num_ftrs = model_ft.classifier[-1].in_features
        model_ft.classifier[-1] = nn.Linear(num_ftrs, 2)

        summary(model_ft, input_size=(3, 224, 224), device='cpu')

        model_ft = model_ft.to(device)

        criterion = nn.CrossEntropyLoss()
        optimizer_ft = optim.SGD(model_ft.parameters(), lr=0.001, momentum=0.9)
        exp_lr_scheduler = lr_scheduler.StepLR(optimizer_ft, step_size=7, gamma=0.1)

        model_ft = train_model(model_ft, criterion, optimizer_ft, exp_lr_scheduler, num_epochs=10)
        visualize_model(model_ft)

        model_conv = torchvision.models.resnet18(pretrained=True)

for index, param in enumerate(model_conv.parameters()):
    if index < 54:
        param.requires_grad = False

num_ftrs = model_conv.fc.in_features
model_conv.fc = nn.Linear(num_ftrs, 2)

for index, param in enumerate(model_ft.parameters()):
    print(index,param.requires_grad)

    summary(model_conv, input_size=(3, 224, 224), device='cpu')

    model_conv = model_conv.to(device)

criterion = nn.CrossEntropyLoss()

optimizer_conv = optim.SGD(model_conv.fc.parameters(), lr=0.001, momentum=0.9)
exp_lr_scheduler = lr_scheduler.StepLR(optimizer_conv, step_size=7, gamma=0.1)

model_conv = train_model(model_conv, criterion, optimizer_conv, exp_lr_scheduler, num_epochs=10)

visualize_model(model_conv)

plt.ioff()
plt.show()
    '''
    return ""