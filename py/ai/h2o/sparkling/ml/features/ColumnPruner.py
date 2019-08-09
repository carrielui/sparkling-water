#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from pyspark import keyword_only
from pyspark.ml.param.shared import *
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaTransformer

from ai.h2o.sparkling import Initializer
from ai.h2o.sparkling.sparkSpecifics import get_input_kwargs


class ColumnPruner(JavaTransformer, JavaMLReadable, JavaMLWritable):
    keep = Param(Params._dummy(), "keep", "keep the specified columns in the frame")

    columns = Param(Params._dummy(), "columns", "specified columns")

    @keyword_only
    def __init__(self, keep=False, columns=[]):
        Initializer.load_sparkling_jar()
        super(ColumnPruner, self).__init__()
        self._java_obj = self._new_java_obj("ai.h2o.sparkling.ml.features.ColumnPruner", self.uid)
        self._setDefault(keep=False, columns=[])
        kwargs = get_input_kwargs(self)
        self.setParams(**kwargs)

    @keyword_only
    def setParams(self, keep=False, columns=[]):
        kwargs = get_input_kwargs(self)
        return self._set(**kwargs)

    def setKeep(self, value):
        return self._set(keep=value)

    def setColumns(self, value):
        return self._set(columns=value)

    def getKeep(self):
        self.getOrDefault(self.keep)

    def getColumns(self):
        self.getOrDefault(self.columns)