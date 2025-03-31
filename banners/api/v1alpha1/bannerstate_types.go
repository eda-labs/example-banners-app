/*
Copyright 2025.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package v1alpha1

import (
    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
)

// BannerStateSpec defines the desired state of BannerState
type BannerStateSpec struct {
    // +eda:ui:title="Nodes"
    // List of TopoNodes this login banner has been applied to
    Nodes []string `json:"nodes,omitempty"`
}

// BannerStateStatus defines the observed state of BannerState
type BannerStateStatus struct {
}

// +kubebuilder:object:root=true
// +kubebuilder:subresource:status
// +kubebuilder:resource:path=bannerstates,scope=Namespaced

// BannerState is the Schema for the bannerstates API
type BannerState struct {
    metav1.TypeMeta   `json:",inline"`
    metav1.ObjectMeta `json:"metadata,omitempty"`

    Spec   BannerStateSpec   `json:"spec,omitempty"`
    Status BannerStateStatus `json:"status,omitempty"`
}

// +kubebuilder:object:root=true

// BannerStateList contains a list of BannerState
type BannerStateList struct {
    metav1.TypeMeta `json:",inline"`
    metav1.ListMeta `json:"metadata,omitempty"`
    Items           []BannerState `json:"items"`
}

func init() {
    SchemeBuilder.Register(&BannerState{}, &BannerStateList{})
}
