import torch
import keyword
import numpy as np
import torchvision
import decord as de
from torch.utils.tensorboard import SummaryWriter
from torchvision import datasets, transforms
from pathlib import Path


def main():
    here = Path(__file__).parent.resolve()
    log_dir = here.parent / 'runs' / 'logs'
    writer = SummaryWriter(log_dir=str(log_dir))

    transform = transforms.Compose(
        [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
    trainset = datasets.MNIST(
        'mnist_train', train=True, download=True, transform=transform)
    trainloader = torch.utils.data.DataLoader(
        trainset, batch_size=64, shuffle=True)
    model = torchvision.models.resnet50(False)
    # Have ResNet model take in grayscale rather than RGB
    model.conv1 = torch.nn.Conv2d(
        1, 64, kernel_size=7, stride=2, padding=3, bias=False)
    images, labels = next(iter(trainloader))

    grid = torchvision.utils.make_grid(images)
    writer.add_image('images', grid, 0)
    writer.add_graph(model, images)
    r = 5

    for n_iter in range(100):
        writer.add_scalar('Loss/train', np.random.random(), n_iter)
        writer.add_scalar('Loss/test', np.random.random(), n_iter)
        writer.add_scalar('Accuracy/train', np.random.random(), n_iter)
        writer.add_scalar('Accuracy/test', np.random.random(), n_iter)
        writer.add_scalar('y=2x', n_iter * 2, n_iter)
        writer.add_scalars('run_14h', {'xsinx': n_iter*np.sin(n_iter/r),
                                       'xcosx': n_iter*np.cos(n_iter/r),
                                       'tanx': np.tan(n_iter/r)}, n_iter)

        writer.add_text('lstm', 'This is an lstm', 0)
        writer.add_text('rnn', 'This is an rnn', 10)

    for i in range(10):
        x = np.random.random(1000)
        writer.add_histogram('distribution centers', x + i, i)
        # writer.close()

    meta = []
    while len(meta) < 100:
        meta = meta+keyword.kwlist  # get some strings
    meta = meta[:100]

    for i, v in enumerate(meta):
        meta[i] = v+str(i)

    label_img = torch.rand(100, 3, 10, 32)
    for i in range(100):
        label_img[i] *= i/100.0

    writer.add_embedding(torch.randn(
        100, 5), metadata=meta, label_img=label_img)
    writer.add_embedding(torch.randn(100, 5), label_img=label_img,global_step=20)
    writer.add_embedding(torch.randn(100, 5), metadata=meta,global_step=20)

    vertices_tensor = torch.as_tensor([
        [1, 1, 1],
        [-1, -1, 1],
        [1, -1, -1],
        [-1, 1, -1],
    ], dtype=torch.float).unsqueeze(0)

    colors_tensor = torch.as_tensor([
        [255, 0, 0],
        [0, 255, 0],
        [0, 0, 255],
        [255, 0, 255],
    ], dtype=torch.int).unsqueeze(0)

    faces_tensor = torch.as_tensor([
        [0, 2, 3],
        [0, 3, 1],
        [0, 1, 2],
        [1, 3, 2],
    ], dtype=torch.int).unsqueeze(0)

    writer.add_mesh(
        'my_mesh',
        vertices=vertices_tensor,
        colors=colors_tensor,
        faces=faces_tensor)

    for i in range(5):
        writer.add_hparams({'lr': 0.1*i, 'bsize': i},
                           {'hparam/accuracy': 10*i, 'hparam/loss': 10*i})

    # binary label
    labels = np.random.randint(2, size=100)
    predictions = np.random.rand(100)
    writer.add_pr_curve('pr_curve', labels, predictions, 0)

    layout = {'Taiwan':{'twse':['Multiline',['twse/0050', 'twse/2330']]},
             'USA':{ 'dow':['Margin',   ['dow/aaa', 'dow/bbb', 'dow/ccc']],
                  'nasdaq':['Margin',   ['nasdaq/aaa', 'nasdaq/bbb', 'nasdaq/ccc']]}}

    writer.add_custom_scalars(layout)

    #video_tensor = torch.randn((10,10,3,480,480))
    vr = de.VideoReader('/Users/chenyang/Downloads/novelctrl.mkv',ctx=de.cpu(0))
    de.bridge.set_bridge('torch')
    frames = vr.get_batch(np.arange(1,1000,100))
    frames = frames.permute(0,3,1,2).unsqueeze(0)


    writer.add_video('my_random_video',frames)



    writer.close()


if __name__ == "__main__":
    main()
