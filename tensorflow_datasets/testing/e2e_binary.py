# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

r"""Binary exercising critical workflow of tensorflow datasets.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import app
import tensorflow_datasets as tfds


def main(argv):
  del argv
  mnist, info = tfds.load('mnist', with_info=True)
  print(mnist, info)
  mnist_train = tfds.load('mnist', split='train')
  print(mnist_train)
  cifar10, info = tfds.load('cifar10', with_info=True)
  print(cifar10, info)
  cifar10_np = tfds.dataset_as_numpy(cifar10)
  print(cifar10_np)


if __name__ == '__main__':
  app.run(main)
